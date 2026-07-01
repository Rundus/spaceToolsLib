# --- epochTime.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to store all the Epoch conversions I often do

from datetime import datetime
from numpy import array

def _get_spacepy_lib():
    """
    Lazily set up and return spacepy.pycdf.lib.

    Imported lazily so `import spaceToolsLib` doesn't require spacepy/the
    NASA CDF library unless a CDF-specific function is actually called.

    Returns
    -------
    module
        The spacepy.pycdf.lib module, used for TT2000 <-> datetime
        conversions.
    """
    from spaceToolsLib.setupFuncs.setupSpacepy import setupPYCDF
    setupPYCDF()
    from spacepy.pycdf import lib
    return lib

def dateTimetoTT2000(InputEpoch,inverse):
    """
    Convert an epoch array between Python datetimes and CDF TT2000 values.

    Parameters
    ----------
    InputEpoch : array_like
        Array of either datetime.datetime objects or TT2000 integer/float
        values, depending on `inverse`.
    inverse : bool
        If True, convert TT2000 -> datetime. If False, convert
        datetime -> TT2000.

    Returns
    -------
    numpy.ndarray
        The converted epoch array.
    """
    lib = _get_spacepy_lib()

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
    """
    Convert an epoch array into seconds elapsed since a reference time T0.

    Parameters
    ----------
    InputEpoch : array_like
        Array of either datetime.datetime objects or TT2000 integer/float
        values.
    T0 : datetime.datetime or int or float
        The reference ("zero") time. Must be a datetime, or a TT2000 value
        (must be >= 1e6, used as a sanity check to catch non-TT2000 input).

    Returns
    -------
    numpy.ndarray
        InputEpoch expressed as seconds elapsed since T0.
    """
    lib = _get_spacepy_lib()

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