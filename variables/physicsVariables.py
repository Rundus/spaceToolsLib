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
IonMasses = [1.67E-27, 2.6567E-26, 1.6738E-27, 6.646477E-27, 5.3134E-26, 4.9826E-26, 2.3259E-26,   4.6518E-26]
ionNames =  ['proton',       'O+',       'H+',        'He+',      'O2+',      'NO+',       'N+',   'N2+']
ep0 = 8.8541878128E-12 # permittivity of free space
u0 = 4*(3.1415926535)*(10**(-7))
lightSpeed = 299792458