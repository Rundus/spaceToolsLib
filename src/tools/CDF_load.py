# --- CDF_load.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to store all the functions I used to load CDFs

from glob import glob
from spaceToolsLib.variables.fliers import fliers
from spaceToolsLib.setupFuncs.setupSpacepy import setupPYCDF
setupPYCDF()
from spacepy import pycdf

def getInputFiles(rocketFolderPath, wRocket, inputPath_modifier, **kwargs):

    modifier = kwargs.get('modifier', '')
    inputFiles = glob(f'{rocketFolderPath}{inputPath_modifier}\{modifier}\{fliers[wRocket - 4]}\*.cdf')
    input_names = [ifile.replace(f'{rocketFolderPath}{inputPath_modifier}\{modifier}\{fliers[wRocket - 4]}\\', '') for ifile in inputFiles]
    input_names_searchable = [ifile.replace(inputPath_modifier.lower() + '_', '') for ifile in input_names]

    return inputFiles,input_names,input_names_searchable

def loadDictFromFile(inputFilePath, **kwargs):

    input_data_dict = kwargs.get('input_data_dict', {})
    globalAttrs = {}
    targetVar = kwargs.get('targetVar', [])
    getGlobalAttrs = kwargs.get('getGlobalAttrs', False)
    reduceData = True if targetVar != [] else kwargs.get('reduceData', False)
    wKeys_Load = kwargs.get('wKeys_Load', [])
    wKeys_Reduce = kwargs.get('wKeys_Reduce', [])

    # load the data dict
    with pycdf.CDF(inputFilePath) as inputDataFile:
        for key, val in inputDataFile.attrs.items():
            globalAttrs = {**globalAttrs, **{str(key): str(val)}}

        for key, val in inputDataFile.items():
            input_data_dict = {**input_data_dict, **{key: [inputDataFile[key][...], {key: val for key, val in inputDataFile[key].attrs.items()}]}}

    # load only the data in wKeys_Load
    output_data_dict = {}
    wKeys_Load = [key for key in input_data_dict.keys()] if wKeys_Load == [] else wKeys_Load
    for key in wKeys_Load:
        output_data_dict = {**output_data_dict, **{key:input_data_dict[key]}}

    # reduce the data
    if reduceData:
        try:
            h = input_data_dict[targetVar[1]]
        except:
            raise Exception(f'no Target Variable found: {targetVar[1]}')

        lowerIndex,higherIndex = abs(output_data_dict[targetVar[1]][0] - targetVar[0][0]).argmin(),abs(output_data_dict[targetVar[1]][0] - targetVar[0][1]).argmin()

        # determine which keys to reduce
        wKeys_Reduce = [key for key in output_data_dict.keys()] if wKeys_Reduce == [] else wKeys_Reduce
        for key in wKeys_Reduce:
            output_data_dict[key][0] = output_data_dict[key][0][lowerIndex:higherIndex]


    if getGlobalAttrs:
        return output_data_dict,globalAttrs
    else:
        return output_data_dict

