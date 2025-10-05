# --- conversions.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to store all the physics conversions I often use


# IMPORTS
from spaceToolsLib.variables.physicsVariables import lat_to_meter,Re
from numpy import cos, radians, pi

def long_to_meter(long, lat):
    return long*(lat_to_meter * cos(radians(lat)))

def meter_to_long(long_km, lat_km):
    latDeg = lat_km/lat_to_meter
    return (long_km/lat_to_meter) * 1/(cos(radians(latDeg)))

def calculateLong_to_meter(Lat): # determines the meters/long conversion for each input lattitude using earth's radius as a perfect sphere
    return (pi/180) * Re * cos(radians(Lat))