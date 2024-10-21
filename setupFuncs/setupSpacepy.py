from os import environ
from spaceToolsLib.setupFuncs import data_paths
def setupPYCDF():
    environ["CDF_LIB"] = data_paths.CDF_LIB