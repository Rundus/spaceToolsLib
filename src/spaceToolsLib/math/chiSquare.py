# --- fit.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to store some fit functions I often use


def calcChiSquare(yData, fitData, yData_errors, fitData_Errors, nu):
    """
    Compute the reduced chi-square statistic between measured data and a fit.

    Parameters
    ----------
    yData : array_like
        Measured/observed data values.
    fitData : array_like
        Corresponding fitted/model values.
    yData_errors : array_like
        Uncertainty on each yData value.
    fitData_Errors : array_like
        Uncertainty on each fitData value.
    nu : int or float
        Number of degrees of freedom to normalize by.

    Returns
    -------
    float
        The reduced chi-square value: sum( (yData - fitData)^2 /
        (yData_errors + fitData_Errors) ) / nu, skipping any terms where
        the summed error is zero.
    """
    chiSum = []

    for i in range(len(yData)):

        if (yData_errors[i] + fitData_Errors[i]) != 0:

            chiSum.append( ((yData[i] - fitData[i])**2) / (yData_errors[i] + fitData_Errors[i])  )

    return (1/nu) * sum(chiSum)