# --- CDF_output.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to store all the functions I used to output CDFs

def outputCDFdata(outputPath, data_dict, **kwargs):
    '''
    Write .cdf file to specified absolute path

    spacetoolslib.outputCDFdata(outputPath, data_dict, **kwargs)

    Paramters:
    [1] outputPath - String with the absolute path of the cdf file destination
    [2] data_dict - dictionariy containing the data to write. Must be in format {'Var Name 1':[DATA1, {'attributeKey1':AttributeVal1, ...}], ...  }
    [3] kwargs - Key word arguments.
        (1) globalAttrsMod - dictionary containing the global attributes of the .cdf file. If none are given, a blank global attributes dictionary is written instead.
        (2) instrNam - Name of the instrument that corresponds to the dataset. If none is given, "none" is written instead.
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