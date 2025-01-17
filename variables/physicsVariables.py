# --- physicsVariables.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to store all the Epoch conversions I often do

m_to_km = 1000
lat_to_meter = 111.319488  # 1 deg latitude to kilometers on Earth
Re = 6357 # radius of earth in kilometer
m_e = 9.11 * 10**(-31)
q0 = 1.602176565 * 10**(-19)
kB = 1.380649 * 10**(-23)
cm_to_m = 100
erg_to_eV = 6.2415E11 # how many eVs are in 1 erg
ep0 = 8.8541878128E-12 # permittivity of free space
u0 = 4*(3.1415926535)*(10**(-7))
lightSpeed = 299792458
gravG = 6.67408E-11
Me = 5.9722E24


# --- --- --- --- --- -
# --- SPACE PHYSICS ---
# --- --- --- --- --- -

# ionospheric ions
amu = 1.660539E-27
ion_dict = {'proton':amu, # proton in kg, same for rest
            'O+':15.999*amu,
            'H+':1.008*amu,
            'He+':4.002*amu,
            'O2+':2*15.999*amu,
            'NO+':(15.999+14.007)*amu,
            'N+':14.007*amu,
            'N2+':14.007*2*amu} # ionospheric ions and their masses

# ionospheric neutrals
netural_dict = {
    'N2': 28.01340*amu,
    'O2':15.999*2*amu,
    'O':15.999*amu,
    'He':4.002*amu,
    'H':1.008*amu,
    'AR':39.95*amu,
    'N':14.007*amu,
    'NO':(15.999+14.007)*amu
}
