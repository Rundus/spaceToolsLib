*******************************************
spaceToolsLib - A Quick Start Documentation
*******************************************

Installation
============

See :doc:`install`.


Loading a .cdf file
===================

Import the module as::
    import spaceToolsLib as stl
    file_path = '(PATH TO YOUR FILE)/fileName.cdf'
    data_dict = stl.loadDictFromFile(file_path)



Data Dictionary Formatting
==========================

spaceToolsLib loads/writes .cdf data as python "data dictionaries" with the following format::
    data_dict = {
                    'variable_name_1':[ numpy.array(YOUR_DATA), {'attribute_name': attribute_value, ...} ],
                    'variable_name_2':[ numpy.array(YOUR_DATA), {'attribute_name': attribute_value, ...} ],
                    .
                    .
                    .
                }


Accessing data in a data dictionary
===================================

The variable data and variable attributes within the Data Dictionary can be accessed through the usual python way.::
    variable_data_1 = data_dict['variable_name_1'][0] # gets the numpy array containing the data
    variable_attributes_1 = data_dict['variable_name_1'][1] # gets the dictonary containing all the attributes for variable 1

    >>> print(variable_data)
    numpy.array(YOUR_DATA)

    >>> print(variable_attributes_1)
    {'attribute_name': attribute_value, ...}


Write a .cdf file
=================
spaceToolsLib writes out .cdf files using Data Dictionaries the same way it loads them. Best practice is to construct a "data_dict_output" python dictionary with whatever data/attributes you need. Global attributes can be specified at the creation of the .cdf file.

The example below uses attributes useful when plotting .cdf files using autoplot, a free open source plotting software.::
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

    global_attributes = {'Mission P.I. Name': 'Someone', ...} # This is line optional

    stl.outputCDFdata(outputPath=file_out_path,
                      data_dict=data_dict_output,
                      globalAttrsMod = global_attributes)