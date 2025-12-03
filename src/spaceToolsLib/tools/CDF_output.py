'''
CDF_output.py

Handles file output functions for spaceToolsLib
Author: C. Feltman
'''


def outputDataDict(outputPath, data_dict, **kwargs):
    '''
    This function writes out a data dictionary to a file. The file's global attributes can also be specified. 
    Default behavior is to overwrite any pre-existing file specified at outputPath.  

    Parameters
    ----------
    outputPath : str
        Absolute path for the file to be written to. File name must end in file extension e.g. (path to file)//your_file.cdf
        Accepted files: .cdf

    data_dict : dict
        python dictionary formatted in the spaceToolsLib way (see github README.md for examples).
        Contains the variable data in numpy arrays and variable attributes as dictionaries.

    globalAttrsMod : dict, optional
        python dictionary containing the global attributes of the file.

    Returns
    -------
    '''

    from os import remove, path
    from spaceToolsLib.setupFuncs.setupSpacepy import (setupPYCDF)
    from spaceToolsLib.variables.exampleMissionAttributes import EXAMPLE_mission_dicts
    setupPYCDF()
    from spacepy import pycdf

    globalAttrsMod = kwargs.get('globalAttrsMod', {})
    instrNam = kwargs.get('instrNam', 'None')

    if globalAttrsMod == {}:
        rocketAttrs = EXAMPLE_mission_dicts()
        globalAttrsMod = rocketAttrs.globalAttributes

    # --- delete output file if it already exists ---
    if path.exists(outputPath):
        remove(outputPath)

    # --- open the output file ---
    with pycdf.CDF(outputPath, '') as sciFile:
        sciFile.readonly(False)
        inputGlobDic = globalAttrsMod

        # # --- write out global attributes ---
        for key, val in inputGlobDic.items():
            if key == 'Descriptor':
                globalAttrsMod[key] = instrNam
            if key in globalAttrsMod:
                sciFile.attrs[key] = globalAttrsMod[key]
            else:
                sciFile.attrs[key] = val

        # --- WRITE OUT DATA ---
        for varKey, varVal in data_dict.items():

            if varKey in ['Epoch', 'Epoch_monitors', 'Epoch_esa']:  # epoch data
                sciFile.new(varKey, data=varVal[0], type=33)
            elif 'Function' in varKey:
                sciFile.new(varKey, data=varVal[0], type=pycdf.const.CDF_REAL8)
            else:  # other data
                sciFile.new(varKey, data=varVal[0])

            # --- Write out the attributes and variable info ---
            for attrKey, attrVal in data_dict[varKey][1].items():
                if attrKey == 'VALIDMIN':
                    sciFile[varKey].attrs[attrKey] = varVal[0].min()
                elif attrKey == 'VALIDMAX':
                    sciFile[varKey].attrs[attrKey] = varVal[0].max()
                elif attrVal != None:
                    sciFile[varKey].attrs[attrKey] = attrVal