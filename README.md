# spaceToolsLib

spaceToolsLib is a python module with many tools to interface with Heliophysics/Space physics data. The module leverages the [spacepy](https://spacepy.github.io/) and [cdflib](https://pypi.org/project/cdflib/) libraries 
to perform many of its underlying functions. This package aims to make reading/writing common file extensions in the space physics community (like .cdf) easy and quick at the cost of customizability. Refer to [spacepy](https://spacepy.github.io/) or [cdflib](https://pypi.org/project/cdflib/) when specific file needs aren't met by spaceToolsLib. 

## Package Highlights

[1] Single-line methods for reading/Writing to NASA Goddard's Common Data Format (.cdf).

[2] No need to specify global or variable attributes while loading/writing .cdf files. 

[3] Built-in colorbars commonly used in the Space Physics Community (MATLAB's Parula, apl rainbow+pink)

[4] Single-line methods to manipulate data (interpolate one dataset onto another, multivariate Singluar Spectrum Analysis, butterworth filtering)

[5] Single-line commands for space-physics related models (CHAOS Geomagnetic field model, 3D Rotation Matrices, Atmospheric Ion Masses) 


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



## Examples

### Loading a .cdf file
```
import spaceToolsLib as stl
file_path = '(PATH TO YOUR FILE)/fileName.cdf'
data_dict = stl.loadDictFromFile(file_path)
```

### Data Dictionary Format
spaceToolsLib loads/writes .cdf data as python "data dictionaries" with the following format
```
data_dict = {
                'variable_name_1':[ numpy.array(YOUR_DATA), {'attribute_name': attribute_value, ...} ],
                'variable_name_2':[ numpy.array(YOUR_DATA), {'attribute_name': attribute_value, ...} ],
                .
                .
                .
            }
```
the variable names within the .cdf file become the keys of the python dictionary (e.g. variable_name_1).

### Accessing data in a data dictionary
The variable data and variable attributes within the Data Dictionary can be accessed through the usual python way.

```
variable_data_1 = data_dict['variable_name_1'][0] # gets the numpy array containing the data
variable_attributes_1 = data_dict['variable_name_1'][1] # gets the dictonary containing all the attributes for variable 1

>>> print(variable_data)
numpy.array(YOUR_DATA)

>>> print(variable_attributes_1)
{'attribute_name': attribute_value, ...}
```

### Writing a .cdf file

spaceToolsLib writes out .cdf files using Data Dictionaries the same way it loads them. Best practice is to construct a "data_dict_output" python dictionary with whatever data/attributes you need. Global attributes can be specified at the creation of the .cdf file.

The example below uses attributes useful when plotting .cdf files using [autoplot](https://autoplot.org/), a free open source plotting software.

```
# some random data
x_data = numpy.array([1,2,3,4,5,6]) 
y_data = numpy.array([1,4,9,16,25,36])

# Construct the data_dict_output
data_dict_output = {
                    'x':[numpy.array(x_data) , {'DEPEND_0':'x_data','LABLAXIS':'x_data'}]
                    'y':[numpy.array(y_data) , {'DEPEND_0':'y_data','LABLAXIS':'y_data'}]
                    }
                    
# create a .cdf file using data_dict_output   

output_file_path = '(PATH TO OUTPUT FILE)/outputFileName.cdf' # path where your .cdf file will go

global_attributes = {'Mission P.I. Name': 'Someone'} # This is line optional

stl.outputCDFdata(outputPath=file_out_path, 
                  data_dict=data_dict_output,
                  globalAttrsMod = global_attributes) 
```


Author: C. Feltman, PhD