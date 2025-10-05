# --- --- --- --- --- --- ---
# --- USER SPECIFIC DATA ---
# --- --- --- --- --- --- ---

# CDF LIB path
from pathlib import Path
configFile_Path = str(Path(__file__).parent) + "\CDF_lib_path.txt" # location to directory that contains the dllcdf.dll needed for pycdf the library
configfile = open(configFile_Path,'r')
CDF_LIB =  configfile.readline()