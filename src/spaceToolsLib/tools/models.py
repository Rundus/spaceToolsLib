# --- models.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to store all the model functions I often use


# Imports
from numpy import radians,power,cos,sqrt,array,exp
from spaceToolsLib.variables.physicsVariables import q0,Re,u0,lightSpeed,m_e,ep0,cm_to_m


# --- Dipole Magnetic Field ---
def Bdip_mag(Alt_km, Lat_deg):
    """
    Compute the magnitude of Earth's dipole magnetic field at a given
    altitude and geomagnetic latitude.

    Parameters
    ----------
    Alt_km : float or array_like
        Altitude above Earth's surface, in kilometers.
    Lat_deg : float or array_like
        Geomagnetic latitude, in degrees.

    Returns
    -------
    float or list of float
        Dipole field magnitude (in Tesla). Returns a list if array-like
        inputs are given, or a single float for scalar inputs.
    """
    B0 = 3.12E-5

    try: # if input data is arrays
        colat = [radians(90 - lat) for lat in Lat_deg]
        Bdip = [B0 * power(Re / (Re + alt), 3) * sqrt(1 + 3 * power(cos(clat), 2)) for alt, clat in zip(Alt_km, colat)]

    except: # if input data is single values
        colat = radians(90 - Lat_deg)
        Bdip = B0 * power(Re / (Re + Alt_km), 3) * sqrt(1 + 3 * power(cos(colat), 2))

    return Bdip


def CHAOS(lat, long, alt, times):
    """
    Compute the geomagnetic field vector at given locations/times using the
    CHAOS geomagnetic field model (core, crustal, and external/induced
    contributions), via the chaosmagpy package.

    Uses the bundled CHAOS .mat model file and RC index .h5 file found in
    supportPackages/CHAOS/.

    Parameters
    ----------
    lat : array_like
        Geographic latitude of each point, in degrees.
    long : array_like
        Geographic longitude of each point, in degrees.
    alt : array_like
        Altitude of each point, in kilometers.
    times : array_like of datetime.date
        Date (year, month, day, hour used) for each point.

    Returns
    -------
    numpy.ndarray
        Array of shape (N, 3) giving the magnetic field vector at each
        point in ENU order: [B_East, B_North, B_Up], in nanotesla.
    """

    # imports
    import datetime as dt
    from glob import glob
    from chaosmagpy import load_CHAOS_matfile
    from chaosmagpy.data_utils import mjd2000
    import chaosmagpy as cp
    from pathlib import Path
    from os.path import dirname


    directoryPath = dirname(Path(__file__).parent) + "/supportPackages/CHAOS/"
    FILEPATH_CHAOS = glob(directoryPath+'/*.mat')[0]
    FILEPATH_RC = glob(directoryPath+'/*.h5')[0]
    cp.basicConfig['file.RC_index'] = FILEPATH_RC

    R_REF = 6371.2

    # give inputs
    theta = array([90 - lat[i] for i in range(len(lat))]) # colat in deg
    phi = array(long)
    radius = array(alt) + R_REF

    # convert datetime date to mjd2000
    if not isinstance(times[0], dt.date):
        raise Exception('Input times are not datetimes. Convert to python datetime')
    else:
        time = array([mjd2000(date.year, date.month, date.day, date.hour) for date in times])  # year, month, day

    # load the CHAOS model
    model = load_CHAOS_matfile(FILEPATH_CHAOS)

    # print('Computing core field.')
    B_core = model.synth_values_tdep(time, radius, theta, phi)

    # print('Computing crustal field up to degree 110.')
    B_crust = model.synth_values_static(radius, theta, phi, nmax=110)

    # complete internal contribution
    B_radius_int = B_core[0] + B_crust[0]
    B_theta_int = B_core[1] + B_crust[1]
    B_phi_int = B_core[2] + B_crust[2]

    # print('Computing field due to external sources, incl. induced field: GSM.')
    B_gsm = model.synth_values_gsm(time, radius, theta, phi, source='all')

    # print('Computing field due to external sources, incl. induced field: SM.')
    B_sm = model.synth_values_sm(time, radius, theta, phi, source='all')

    # complete external field contribution
    B_radius_ext = B_gsm[0] + B_sm[0]
    B_theta_ext = B_gsm[1] + B_sm[1]
    B_phi_ext = B_gsm[2] + B_sm[2]

    # complete forward computation
    B_radius = B_radius_int + B_radius_ext
    B_theta = B_theta_int + B_theta_ext
    B_phi = B_phi_int + B_phi_ext

    # output CHAOS_ENU
    B_ENU = array([[B_phi[i],-1*B_theta[i], B_radius[i]] for i in range(len(B_radius))])

    return B_ENU

def kineticTerm(kperp, z, simplify): # represents the denominator of the Alfven velocity term: 1/(1 + (kperp*c/omega_pe)^2)^1/2
    """
    Compute the kinetic correction term in the denominator of the Alfven
    velocity: 1 / sqrt(1 + (kperp * c / omega_pe)^2).

    Parameters
    ----------
    kperp : float
        Perpendicular wavenumber.
    z : float
        Altitude, passed to the (currently unimplemented) density(z)
        ionospheric density model when simplify=False.
    simplify : bool
        If True, returns the simplified constant 1/sqrt(2) without
        needing a density model. If False, requires a density(z) model
        that is not yet implemented (see Raises).

    Returns
    -------
    float
        The kinetic correction term.

    Raises
    ------
    NotImplementedError
        If simplify=False, since this branch depends on a density(z)
        ionospheric density model not yet implemented in spaceToolsLib.
    """
    if simplify:
        y = 1/sqrt(2)
    else:
        # NOTE: this branch calls density(z), which is not defined/imported
        # anywhere in spaceToolsLib. This previously raised a silent NameError
        # at call time. Left as an explicit NotImplementedError until a real
        # ionospheric density model is wired in -- do not guess at one here,
        # since an incorrect density model would silently produce wrong physics.
        raise NotImplementedError(
            "kineticTerm(simplify=False) requires a density(z) ionospheric "
            "density model that is not yet implemented in spaceToolsLib. "
            "Use simplify=True, or supply your own density(z) function."
        )
    return y

def AlfvenSpeed(z,lat,long,year,kperp,simplify):
    """
    Compute the Alfven speed at a given location/time, combining the CHAOS
    geomagnetic field model with a kinetic correction term.

    Parameters
    ----------
    z : float
        Altitude, in kilometers.
    lat : float
        Geographic latitude, in degrees.
    long : float
        Geographic longitude, in degrees.
    year : datetime.date
        Date used to evaluate the CHAOS field model.
    kperp : float
        Perpendicular wavenumber, passed to kineticTerm().
    simplify : bool
        Passed to kineticTerm() -- see that function for details.

    Returns
    -------
    float
        The Alfven speed.

    Raises
    ------
    NotImplementedError
        Always currently, since this function depends on a density(z)
        ionospheric density model and an IonMasses source that are not yet
        implemented in spaceToolsLib.
    """
    # -- Output order forpyIGRF.igrf_value ---
    # [0] Declination (+ E | - W)
    # [1] Inclination (+ D | - U)
    # [2] Horizontal Intensity
    # [3] North Comp (+ N | - S)
    # [4] East Comp (+ E | - W)
    # [5] Vertical Comp (+ D | - U)
    # [6] Total Field

    # NOTE: this function calls density(z) and IonMasses, neither of which is
    # defined/imported anywhere in spaceToolsLib. This previously raised a
    # silent NameError at call time. Raising explicitly here until a real
    # ionospheric density model and ion mass source are wired in -- do not
    # guess at values here, since incorrect ones would silently produce wrong physics.
    raise NotImplementedError(
        "AlfvenSpeed() requires a density(z) ionospheric density model and an "
        "IonMasses source that are not yet implemented in spaceToolsLib. "
        "See tools/models.py."
    )