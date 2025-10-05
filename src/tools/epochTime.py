# --- epochTime.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to store all the Epoch conversions I often do

from datetime import datetime
from numpy import array
from spaceToolsLib.setupFuncs.setupSpacepy import setupPYCDF
setupPYCDF()
from spacepy.pycdf import lib

def dateTimetoTT2000(InputEpoch,inverse):

    if inverse: # tt2000 to datetime
        if isinstance(InputEpoch[0], datetime):
            raise Exception(TypeError, "Input Epoch Array is datetime array!")
        else:
            return array([lib.tt2000_to_datetime(tme) for tme in InputEpoch])
    else: # datetime to tt2000
        if isinstance(InputEpoch[0], (int, float, complex)):
            raise Exception(TypeError, "Input Epoch Array is TT2000 array!")
        else:
            return array([lib.datetime_to_tt2000(tme) for tme in InputEpoch])


def EpochTo_T0_Rocket(InputEpoch, T0):

    # Convert the T0
    if isinstance(T0, datetime):  # Input Epoch is datetime array
        startPoint = lib.datetime_to_tt2000(T0)
    elif isinstance(T0, (int, float, complex)):
        if T0 < 1E6: # if T0 is an integter but small-ish, then it's not a tt2000
            raise Exception('T0 is not a TT2000 Value')
        else: # If T0 is already a TT2000
            startPoint = T0

    # Convert the Epoch
    if isinstance(InputEpoch[0],datetime): # Input Epoch is datetime array
        return array([lib.datetime_to_tt2000(tme) - startPoint for tme in InputEpoch])/1E9
    elif isinstance(InputEpoch[0], (int, float, complex)): # Input Epoch is tt2000 array
        return (array(InputEpoch) - startPoint)/1E9