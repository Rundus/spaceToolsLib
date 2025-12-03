# --- filter.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to store all the Filtering functions I use
import numpy as np
# imports
from scipy.signal import butter, filtfilt
from numpy import (ndarray,array, arange,outer,zeros,identity,flip)
from numpy.linalg import svd,matrix_rank
from pandas import Series,DataFrame


class butterFilter:
    def butterworth(self,lowcutoff, highcutoff, fs, order, filtertype):
        if filtertype.lower() == 'bandpass':
            return butter(N = order, Wn = [lowcutoff, highcutoff], fs=fs, btype='bandpass')
        elif filtertype.lower() == 'lowpass':
            return butter(N=order, Wn = highcutoff, fs=fs, btype='lowpass')
        elif filtertype.lower() == 'highpass':
            return butter(N=order, Wn = lowcutoff, fs=fs, btype='highpass')
        elif filtertype.lower() == 'bandstop':
            return butter(N=order, Wn = [lowcutoff, highcutoff], fs=fs, btype='bandstop')
    def butter_filter(self,data, lowcutoff, highcutoff, fs, order,filtertype):
        b, a = self.butterworth(lowcutoff, highcutoff, fs, order, filtertype)
        y = filtfilt(b, a, data)
        return y


class SSA(object):

    """
    CODE SOURCE: https://www.kaggle.com/code/jdarcy/introducing-ssa-for-time-series-decomposition
    """
    __supported_types = (Series, ndarray, list)
    def __init__(self, tseries, L, save_mem=True, **kwargs):
        """
        Decomposes the given time series with a singular-spectrum analysis. Assumes the values of the time series are
        recorded at equal intervals.

        Parameters
        ----------
        tseries : The original time series, in the form of a Pandas Series, NumPy array or list.
        L : The window length. Must be an integer 2 <= L <= N/2, where N is the length of the time series.
        save_mem : Conserve memory by not retaining the elementary matrices. Recommended for long time series with
            thousands of values. Defaults to True.
            
        Optional
        --------
        mirror_percent : float
            between 0 and 1 representing the amount of data to mirror/reflect on the starting/end of the dataset to avoid edge effects of the filter


        Note: Even if an NumPy array or list is used for the initial time series, all time series returned will be
        in the form of a Pandas Series or DataFrame object.
        """

        # Tedious type-checking for the initial time series
        if not isinstance(tseries, self.__supported_types):
            raise TypeError("Unsupported time series object. Try Pandas Series, NumPy array or list.")
        
                
        # Add in the mirrored data
        if kwargs.get('mirror_percent', False) != False:
            self.mirrorPercent = kwargs.get('mirror_percent', False)
            self.original_length = len(tseries) # used later on, but stored now
            self.addThisMuchIndex = int(self.mirrorPercent*len(tseries))
            self.firstHalf = list(flip(array(tseries[0:self.addThisMuchIndex])))
            self.backHalf = list(flip(array(tseries[-self.addThisMuchIndex:])))
            self.mirroredData = array(self.firstHalf + list(tseries) + self.backHalf)
            tseries = self.mirroredData
        
        # Checks to save us from ourselves
        self.N = len(tseries)
        if not 2 <= L <= self.N / 2:
            raise ValueError("The window length must be in the interval [2, N/2].")

        self.L = L
        self.orig_TS = Series(tseries)
        self.K = self.N - self.L + 1

        # Embed the time series in a trajectory matrix
        self.X = array([self.orig_TS.values[i:L + i] for i in range(0, self.K)]).T

        # Decompose the trajectory matrix
        self.U, self.Sigma, VT = svd(self.X)
        self.d = matrix_rank(self.X)

        self.TS_comps = zeros((self.N, self.d))

        if not save_mem:
            # Construct and save all the elementary matrices
            self.X_elem = array([self.Sigma[i] * outer(self.U[:, i], VT[i, :]) for i in range(self.d)])

            # Diagonally average the elementary matrices, store them as columns in array.
            for i in range(self.d):
                X_rev = self.X_elem[i, ::-1]
                self.TS_comps[:, i] = [X_rev.diagonal(j).mean() for j in range(-X_rev.shape[0] + 1, X_rev.shape[1])]

            self.V = VT.T

        else:
            # Reconstruct the elementary matrices without storing them
            for i in range(self.d):
                X_elem = self.Sigma[i] * outer(self.U[:, i], VT[i, :])
                X_rev = X_elem[::-1]
                self.TS_comps[:, i] = [X_rev.diagonal(j).mean() for j in range(-X_rev.shape[0] + 1, X_rev.shape[1])]

            self.X_elem = "Re-run with save_mem=False to retain the elementary matrices."

            # The V array may also be very large under these circumstances, so we won't keep it.
            self.V = "Re-run with save_mem=False to retain the V matrix."

        # If data was mirrored, reduce the mirror percentage
        if kwargs.get('mirror_percent', False) != False:                          
            self.TS_comp = self.TS_comps[self.addThisMuchIndex:self.addThisMuchIndex+self.original_length,:]
            
        # Calculate the w-correlation matrix.
        self.calc_wcorr()

    def components_to_df(self, n=0):
        """
        Returns all the time series components in a single Pandas DataFrame object.
        """
        if n > 0:
            n = min(n, self.d)
        else:
            n = self.d

        # Create list of columns - call them F0, F1, F2, ...
        cols = ["F{}".format(i) for i in range(n)]
        return DataFrame(self.TS_comps[:, :n], columns=cols, index=self.orig_TS.index)
    def reconstruct(self, indices):
        """
        Reconstructs the time series from its elementary components, using the given indices. Returns a Pandas Series
        object with the reconstructed time series.

        Parameters
        ----------
        indices: An integer, list of integers or slice(n,m) object, representing the elementary components to sum.
        """
        if isinstance(indices, int): indices = [indices]

        ts_vals = self.TS_comps[:, indices].sum(axis=1)
        return Series(ts_vals, index=self.orig_TS.index)
    def calc_wcorr(self):
        """
        Calculates the w-correlation matrix for the time series.
        """

        # Calculate the weights
        w = array(list(arange(self.L) + 1) + [self.L] * (self.K - self.L - 1) + list(arange(self.L) + 1)[::-1])

        def w_inner(F_i, F_j):
            return w.dot(F_i * F_j)

        # Calculated weighted norms, ||F_i||_w, then invert.
        F_wnorms = array([w_inner(self.TS_comps[:, i], self.TS_comps[:, i]) for i in range(self.d)])
        F_wnorms = F_wnorms ** -0.5

        # Calculate Wcorr.
        self.Wcorr = identity(self.d)
        for i in range(self.d):
            for j in range(i + 1, self.d):
                self.Wcorr[i, j] = abs(w_inner(self.TS_comps[:, i], self.TS_comps[:, j]) * F_wnorms[i] * F_wnorms[j])
                self.Wcorr[j, i] = self.Wcorr[i, j]
        return self.Wcorr
    def plot_wcorr(self, min=None, max=None):
        import matplotlib.pyplot as plt
        """
        Plots the w-correlation matrix for the decomposed time series.
        """
        if min is None:
            min = 0
        if max is None:
            max = self.d

        if self.Wcorr is None:
            self.calc_wcorr()

        ax = plt.imshow(self.Wcorr, cmap='turbo')
        plt.xlabel(r"$\tilde{F}_i$")
        plt.ylabel(r"$\tilde{F}_j$")
        plt.colorbar(ax.colorbar, fraction=0.045)
        ax.colorbar.set_label("$W_{i,j}$")
        plt.clim(0, 1)

        # For plotting purposes:
        if max == self.d:
            max_rnge = self.d - 1
        else:
            max_rnge = max

        plt.xlim(min - 0.5, max_rnge + 0.5)
        plt.ylim(max_rnge + 0.5, min - 0.5)
        
    def plot_components(self, wComponents,**kwargs):
        '''
        Parameters
        ----------
        wComponents : ndarray
            Array of indices corresponding to the eigenvectors "F"
            
        kwargs
        ------        
        wGroups : ndarray
            array of lists containing the indices in wComponents which have their eigenvectors summed together when plotted
        
        '''        
        
        # get the eignvectors
        eigen_vectors = self.components_to_df()                        
        
        # determine which eigenvectors are plotted and which aren't
        values = [i for i in range(self.L)] # all the indices
        non_specified = [val for val in values if val not in wComponents]

        # construct the original signal for comparison
        original_tseries = self.reconstruct(values)
                
        # prepare the data for plotting        
        if kwargs.get('wGroups', False):
            groupings = {}
            for group in kwargs.get('wGroups', False):                
                key_name = f'F'
                key_data = np.zeros(shape=np.shape(eigen_vectors['F0']))
                for group_idx in group:
                    key_name += str(group_idx)     
                    key_data += eigen_vectors[f'F{group_idx}']                
                groupings = {**groupings, **{key_name:key_data}}
        else:
            groupings = {f'F{i}':eigen_vectors[f'F{i}'] for i in wComponents}                        
        
        self.the_rest = self.reconstruct(indices=non_specified)
        groupings = {**groupings,**{'$F_{remaining}$':self.the_rest}}            

        #############################
        # --- plot the components ---
        #############################
        import matplotlib.pyplot as plt
        self.num = len(groupings.keys())
        fig, ax = plt.subplots(self.num+1)
        
        # plot the original signal
        ax[0].plot(original_tseries)
        ax[0].set_ylabel('Original')
        
        # plot the remain vectors
        self.counter = 1
        for key, val in groupings.items():
            ax[self.counter].plot(val)
            ax[self.counter].set_ylabel(f"{key}")
            self.counter += 1
        plt.tight_layout()        

class mSSA:
    def mSSA_components(self, data_dict_input, compNames, SSA_window_Size, mirrorData, **kwargs):

        '''

        Parameters
        ----------
        data_dict_input : dict
        compNames : bytearray
        SSA_window_Size : int
        mirrorData : bool

        kwargs
        ------
        mirrorPercent : float
            float between 0 to 1 representing the amount of data to mirror/reflect on the starting/end of the dataset to avoid edge effects of the filter

        returns
        -------
        data_dict

        '''

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

        # create the output data_dict and populate it
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

    def generateGrouping(self, SSA_window_Size, badCompIndicies, InvestigateIndicies, noiseLimit):

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

    # def mSSA_wCorMatrix_Plotting(self, B_SSA, grouping, SSA_window_Size,compNames):
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