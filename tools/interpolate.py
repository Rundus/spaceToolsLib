# --- interpolate.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to store all the classes/variables/functions



# Imports
from numpy import array
from spaceToolsLib.setupFuncs.setupSpacepy import setupPYCDF
setupPYCDF()
from spacepy.pycdf import lib

# Variables

def InterpolateDataDict(InputDataDict,InputEpochArray,wKeys,targetEpochArray):

    # InputDataDict --> Contains a data_dict of the data which will be interpolated onto the new dataset
    # InputEpoch --> The epoch that InputDataDict uses
    # wKeys --> Keys of the variables in InputDataDict that we want to interpolate. If wKeys == [], do all the keys
    # targetEpoch --> Epoch that the data will be interpolated onto (MUST BE IN TT2000)

    from scipy.interpolate import CubicSpline
    import datetime as dt

    # get the keys to interpolate
    if wKeys == []:
        wKeys = [key for key, val in InputDataDict.items()]

    # Ensure the inputEpoch is in tt2000
    if isinstance(InputEpochArray[0], dt.datetime):
        InputEpochArray = array([lib.datetime_to_tt2000(tme) for tme in InputEpochArray])
    if isinstance(targetEpochArray[0], dt.datetime):
        targetEpochArray = array([lib.datetime_to_tt2000(tme) for tme in targetEpochArray])


    # --- Do the interpolation ---
    data_dict_interpolated = {}

    # interpolate over all the keys and store them in new dictonary
    for key in wKeys:
        if 'Epoch'.lower() not in key.lower():

            # --- cubic interpolation ---
            splCub = CubicSpline(InputEpochArray, InputDataDict[key][0])

            # --- evaluate the interpolation at all the new Epoch points ---
            newData = array([splCub(timeVal) for timeVal in targetEpochArray])

            # --- store the data in the interpolated data_dict ---
            data_dict_interpolated = {**data_dict_interpolated, **{key:[newData,InputDataDict[key][1]]}}

        else:
            newEpoch = array([lib.tt2000_to_datetime(tme) for tme in targetEpochArray])
            data_dict_interpolated = {**data_dict_interpolated, **{key:[newEpoch,InputDataDict[key][1]]}}

    return data_dict_interpolated