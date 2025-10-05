# spaceToolsLib

spaceToolsLib is a python module with many tools to interface with Heliophysics/Space physics data. The module leverages the [spacepy](https://spacepy.github.io/) and [cdflib](https://pypi.org/project/cdflib/) libraries 
to perform many of its underlying functions. This package aims to make reading/writing common file extensions in the space physics community (like .cdf) easy and quick at the cost of customizability. Refer to [spacepy](https://spacepy.github.io/) or [cdflib](https://pypi.org/project/cdflib/) when specific file needs aren't met by spaceToolsLib. 

Package highlights include

[1] Reading/Writing to NASA Goddard's Common Data Format (.cdf) files with single-line commands.

[2] Built-in colorbars commonly used in the Space Physics Community (MATLAB's Parula, apl rainbow+pink)

[3] Single-line methods to manipulate data (interpolate one dataset onto another, multivariate Singluar Spectrum Analysis, butterworth filtering)

[4] Single-line commands for space-physics related models (CHAOS Geomagnetic field model, 3D Rotation Matrices, Atmospheric Ion Masses) 


## **Install**
To install, open up your python terminal/command prompt and type:

```
pip install -i https://test.pypi.org/simple/spaceToolsLib
```

### Installation notes

**(Required)** This package requires the NASA CDF function library, found here: [NASA CDF Library](https://cdf.gsfc.nasa.gov/). Download this folder, place it most anywhere but note it's file path.

**(Required)** After package installation, open "../spaceToolsLib/setupFuncs/CDF_lib_path.txt" and update with the absolute path of the NASA CDF libray "(PATH TO NASA CDF LIBRARY)/lib" directory.

(Note: The spacepy module is looking for the libcdf.dll file in the "lib" directory. Windows users may need to ensure this file exists in the provided NASA file.)
## Dependencies
[1] [spacepy](https://spacepy.github.io/)

[2] [cdflib](https://pypi.org/project/cdflib/)

[3] numpy (any version)

[3] [The NASA CDF Library](https://cdf.gsfc.nasa.gov/)

The spaceToolsLib source code here on [git](https://github.com/Rundus/spaceToolsLib). 


Author: C. Feltman, PhD