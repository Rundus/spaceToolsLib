from os import environ
from spaceToolsLib.setupFuncs import data_paths
def setupPYCDF():
    """
    Point spacepy's pycdf module at the user-configured NASA CDF library.

    Reads the path stored in setupFuncs/CDF_lib_path.txt (via
    data_paths.CDF_LIB) and sets the CDF_LIB environment variable to it,
    which spacepy.pycdf requires to locate the NASA CDF C library at import
    time. Must be called before `from spacepy import pycdf`.

    Returns
    -------
    None
    """
    environ["CDF_LIB"] = data_paths.CDF_LIB