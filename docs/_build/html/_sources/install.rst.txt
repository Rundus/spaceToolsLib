************************
Installing spaceToolsLib
************************

If you already have a working Python setup, open up your python terminal/command prompt and type:
  ``pip install -i https://test.pypi.org/simple/spaceToolsLib``

Installation notes
(Required) This package requires the `NASA CDF function library <https://cdf.gsfc.nasa.gov/>`_. Download this folder, place it most anywhere but note it's file path.

(Required) After package installation, open "../spaceToolsLib/setupFuncs/CDF_lib_path.txt" and update with the absolute path of the NASA CDF libray "(PATH TO NASA CDF LIBRARY)/lib" directory.

(Note: The spacepy module is looking for the libcdf.dll file in the "lib" directory. Windows users may need to ensure this file exists in the provided NASA file.)


Troubleshooting
===============

Contact cfeltman@uiowa.edu for assistance.