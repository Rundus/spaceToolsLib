'''
CDF_load.py

Handles file input functions for spaceToolsLib
Author: C. Feltman
'''

from glob import glob
from spaceToolsLib.setupFuncs.setupSpacepy import setupPYCDF
setupPYCDF()
from spacepy import pycdf

def loadDictFromFile(inputFilePath, **kwargs):

    """
    This function loads a .cdf file and returns a spaceToolsLib data_dictionary containing
    the variable names, data and attributes. The file's global attributes can also be returned.

    :param inputFilePath: Absolute path of the file to load. Accepted files: .cdf
    :type inputFilePath: str

    :param getGlobalAttrs: Optional, if True, returns the global attributes of the file as a python dictionary as well as the data dictionary
    :type getGlobalAttrs: bool

    :return data_dictionary: Python dictionary containing the file variable data and variable attributes. If getGlobalAttrs == True then
        a tuple containing both the data_dict and global attributes is returned (data_dict, globalAttrs).
    :rtype: dict
    """

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

