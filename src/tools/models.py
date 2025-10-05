# --- models.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to store all the model functions I often use


# Imports
from numpy import radians,power,cos,sqrt,array,exp
from spaceToolsLib.variables.physicsVariables import q0,Re,u0,lightSpeed,m_e,ep0,cm_to_m


# --- Dipole Magnetic Field ---
def Bdip_mag(Alt_km, Lat_deg):
    B0 = 3.12E-5

    try: # if input data is arrays
        colat = [radians(90 - lat) for lat in Lat_deg]
        Bdip = [B0 * power(Re / (Re + alt), 3) * sqrt(1 + 3 * power(cos(clat), 2)) for alt, clat in zip(Alt_km, colat)]

    except: # if input data is single values
        colat = radians(90 - Lat_deg)
        Bdip = B0 * power(Re / (Re + Alt_km), 3) * sqrt(1 + 3 * power(cos(colat), 2))

    return Bdip


def CHAOS(lat, long, alt, times):

    # imports
    import datetime as dt
    from glob import glob
    from chaosmagpy import load_CHAOS_matfile
    from chaosmagpy.data_utils import mjd2000
    from pathlib import Path
    from os.path import dirname

    directoryPath = dirname(Path(__file__).parent) + "\supportPackages\CHAOS\\"
    FILEPATH_CHAOS = glob(directoryPath+'\*.mat')[0]

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
    if simplify:
        y = 1/sqrt(2)
    else:
        plasmaFreq = sqrt((density(z) * q0 * q0) / (m_e * ep0))
        y = 1 / sqrt(1 + (kperp * lightSpeed / plasmaFreq) ** 2)
    return y

def AlfvenSpeed(z,lat,long,year,kperp,simplify):
    # -- Output order forpyIGRF.igrf_value ---
    # [0] Declination (+ E | - W)
    # [1] Inclination (+ D | - U)
    # [2] Horizontal Intensity
    # [3] North Comp (+ N | - S)
    # [4] East Comp (+ E | - W)
    # [5] Vertical Comp (+ D | - U)
    # [6] Total Field

    B = CHAOS(lat, long, z, year)
    V_A = (B[6]*1E-9)/sqrt(u0 * density(z) * IonMasses[0])

    if simplify:
        V = V_A*kineticTerm(1, z, simplify)
    else:
        V = V_A*kineticTerm(kperp, z, simplify)
    return V