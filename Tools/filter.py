# --- filter.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to store all the Filtering functions I use



# imports
from scipy.signal import butter, filtfilt
from numpy import flip,array

def butterworth(lowcutoff, highcutoff, fs, order, filtertype):
    if filtertype.lower() == 'bandpass':
        return butter(N = order, Wn = [lowcutoff, highcutoff], fs=fs, btype='bandpass')
    elif filtertype.lower() == 'lowpass':
        return butter(N=order, Wn = highcutoff, fs=fs, btype='lowpass')
    elif filtertype.lower() == 'highpass':
        return butter(N=order, Wn = lowcutoff, fs=fs, btype='highpass')
    elif filtertype.lower() == 'bandstop':
        return butter(N=order, Wn = [lowcutoff, highcutoff], fs=fs, btype='bandstop')
def butter_filter(data, lowcutoff, highcutoff, fs, order,filtertype):
    b, a = butterworth(lowcutoff, highcutoff, fs, order, filtertype)
    y = filtfilt(b, a, data)
    return y

def mSSA_components(data_dict_input, compNames, SSA_window_Size, mirrorData, **kwargs):

    # Functionality Statement:
    # [1] Input a data_dict
    # [2] Identify the components to mSSA
    # [3] If you need to mirror the data first, do so
    # [4] Calculate the mSSA components
    # [5] return a new data_dict with the Epoch variable also inside

    # get kwargs
    mirrorPercent = kwargs.get('mirrorPercent', 0.2)

    # --- Imports ---
    from spaceToolsLib.supportPackages.pymssa.mssa import MSSA
    from pandas import DataFrame
    from copy import deepcopy

    # --- Ensure all the compNames keys are in the data_dict_input ---
    for key in compNames:
        if key not in data_dict_input:
            raise Exception('input Variable Key not in data dictionary')

    # --- Ensure all the Epoch variable is in the data_dict_input ---
    if 'Epoch' not in data_dict_input:
        raise Exception(r'No variable named "Epoch" in input dictionary')

    # --- Mirror the data if requested ---
    # in order to eliminate the effect of mSSA has on the edge of the dataset when stitching
    # things together, we concatinate 20% of the mirrored data to the sides of the dataset
    if mirrorData:
        for key in compNames:
            inputData = array(deepcopy(data_dict_input[key][0]))
            addThisMuchIndex = int(mirrorPercent*len(inputData))
            firstHalf = list(flip(array(inputData[0:addThisMuchIndex])))
            backHalf = list(flip(array(inputData[-addThisMuchIndex:])))
            mirroredData = array( firstHalf + list(inputData) + backHalf)
            data_dict_input[key][0] = mirroredData

    # --- --- --- --- ----
    # --- PERFORM mSSA ---
    # --- --- --- --- ----

    # create the MSSA object
    mssa = MSSA(n_components=None, window_size=SSA_window_Size, verbose=False)

    # convert data_dict input Data to pandas dataframe
    data = DataFrame({compNames[i]: data_dict_input[compNames[i]][0] for i in range(len(compNames))})

    # calculate the mSSA
    mssa.fit(data)

    # get the mSSA components
    components = mssa.components_

    # --- --- --- --- --- ---
    # --- output the data ---
    # --- --- --- --- --- ---

    # creat the output data_dict and populate it
    data_dict_output = {}

    for i in range(len(compNames)):
        dataToOutput = array(components[i, :, :])  # update the data for output to be the components
        attrs = deepcopy(data_dict_input[compNames[i]][1])
        attrs['LABLAXIS'] = compNames[i]
        attrs['VALIDMIN'] = dataToOutput.min()
        attrs['VALIDMAX'] = dataToOutput.max()
        data_dict_output = {**data_dict_output, **{compNames[i]: [dataToOutput, attrs]}}

    # add in the Epoch variable
    data_dict_output = {**data_dict_output, **{'Epoch': deepcopy(data_dict_input['Epoch'])}}

    return data_dict_output

def generateGrouping(SSA_window_Size, badCompIndicies, InvestigateIndicies, noiseLimit):

    if SSA_window_Size == 0: # if the file I'm working on isn't an SSAcomp file
        return []
    else: # make the proper grouping
        # first plot every component i.e. the original data
        group = [[i for i in range(SSA_window_Size * 3)]]

        # plot all the identified bad inidices
        grouping = [badCompIndicies]

        # investigate other components
        grouping += InvestigateIndicies
        # grouping += [[i] for i in range(9)]

        # the "noise" data
        grouping += [[i for i in range(noiseLimit, 3 * SSA_window_Size)]]

        # # get the good stuff
        goodStuff = []
        for i in range(noiseLimit):
            if i not in grouping[0]:
                goodStuff.append(i)

        grouping += [goodStuff]

        return group + grouping

# def mSSA_wCorMatrix_Plotting(B_SSA, grouping, SSA_window_Size,compNames):
#
#     # --- collect the group info for the LAST (noise) grouping ---
#
#     prgMsg('Plotting wCor Matrix (WARNING: THIS CAN TAKE A LONG TIME):')
#     from ACESII_code.supportPackages.Support_Libraries.pymssa import MSSA
#     from pandas import DataFrame
#
#     mssa = MSSA(n_components=None, window_size=SSA_window_Size, verbose=False)
#
#     # convert data_dict input Data to pandas dataframe
#     data = DataFrame({compNames[i]: data_dict_input[compNames[i]][0] for i in range(len(compNames))})
#
#     # calculate the mSSA
#     mssa.fit(data)
#
#     # plot all three axes correlation matrix
#     mssa.fit(DataFrame(
#         {'Data1': [i for i in range(len(data_dict_SSAcomps['Epoch'][0]))],
#          'Data2': [i for i in range(len(data_dict_SSAcomps['Epoch'][0]))],
#          'Data3': [i for i in range(len(data_dict_SSAcomps['Epoch'][0]))]}
#     ))
#
#     for i in range(3):
#         mssa.components_[i, :, :] = data_dict_SSAcomps[compNames[i]][0]
#
#     for i in range(3):
#         # calculate correlation matrix
#         wcorr = np.abs(mssa.w_correlation(mssa.components_[i, :, :]))
#
#         # plot it
#         plt.title(compNames[i])
#         ax = plt.imshow(wcorr, cmap='turbo')
#         plt.xlabel(r"$\tilde{F}_i$")
#         plt.ylabel(r"$\tilde{F}_j$")
#         plt.colorbar(ax.colorbar, fraction=0.045)
#         ax.colorbar.set_label("$W_{i,j}$")
#         plt.clim(0, 1)
#         plt.show()