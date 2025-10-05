# spaceToolsLib

spaceToolsLib is a python module with many tools to interface with Heliophysics/Space physics data. The module leverages the [spacepy](https://spacepy.github.io/) and [cdflib](https://pypi.org/project/cdflib/) libraries 
to perform many of its underlying functions. 

Highlights include

[1] Reading/Writing CDF (Common Data Format .cdf) files with single-line commands.

[2] MatplotLib built-in colorbars commonly used in the Space Physics Communitites

[3] Several, single-line methods to interface with data (e.g. interpolating one dataset based on another, CHAOS Geomagnetic field model, multivariate Singluar Spectrum Analysis, etc )


## **Install**
To install, open up your terminal/command prompt and type:

```
pip install -i https://test.pypi.org/simple/ spaceToolsLib
```

### Installation notes
Once installed, open the file CDF_lib_path.txt found at "../spaceToolsLib/setupFuncs/CDF_lib_path.txt" in the python module and edit it with the absolute path of the NASA CDF libray "lib" directory. The spacepy module is looking for the "libcdf.dll" file in this directory. Windows users may need to ensure this file exists in the provided NASA files and move it to the right directory if needed.  

## Notes
Notable dependencies:
(1) spacepy, (2) cdflib python modules and (3) The NASA CDF library, found here: [NASA CDF Library](https://cdf.gsfc.nasa.gov/)

The [source Code](https://github.com/Rundus/spaceToolsLib) can be found on git. 


Author: C. Feltman