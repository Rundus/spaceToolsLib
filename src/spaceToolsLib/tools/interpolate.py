# --- interpolate.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to store all the classes/variables/functions



# Imports
from numpy import array

# Variables

def InterpolateDataDict(InputDataDict,InputEpochArray,wKeys,targetEpochArray):
    """
    Cubic-spline interpolate the variables of a spaceToolsLib data
    dictionary from their original epoch onto a new target epoch array.

    Parameters
    ----------
    InputDataDict : dict
        A spaceToolsLib data dictionary containing the data to interpolate.
    InputEpochArray : array_like
        The epoch (TT2000 values or datetime.datetime objects) that
        InputDataDict's data currently uses.
    wKeys : list of str
        Keys of the variables in InputDataDict to interpolate. If [],
        interpolates every key in InputDataDict.
    targetEpochArray : array_like
        The epoch to interpolate onto (TT2000 values or datetime.datetime
        objects).

    Returns
    -------
    dict
        A new data dictionary with each requested variable's data
        interpolated (via scipy.interpolate.CubicSpline) onto
        targetEpochArray. Any key containing 'Epoch' is instead replaced
        directly with targetEpochArray (converted to datetime).
    """

    from scipy.interpolate import CubicSpline
    import datetime as dt

    # imported lazily so `import spaceToolsLib` doesn't require spacepy/the
    # NASA CDF library unless a CDF-specific function is actually called
    from spaceToolsLib.setupFuncs.setupSpacepy import setupPYCDF
    setupPYCDF()
    from spacepy.pycdf import lib

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