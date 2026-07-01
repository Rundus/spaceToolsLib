# --- conversions.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to store all the physics conversions I often use


# IMPORTS
from spaceToolsLib.variables.physicsVariables import lat_to_meter,Re
from numpy import cos, radians, pi

def long_to_meter(long, lat):
    """
    Convert a longitude distance (in degrees) to kilometers at a given latitude.

    Parameters
    ----------
    long : float or array_like
        Longitude distance, in degrees.
    lat : float or array_like
        Latitude at which the conversion is evaluated, in degrees.

    Returns
    -------
    float or array_like
        Equivalent distance in kilometers.
    """
    return long*(lat_to_meter * cos(radians(lat)))

def meter_to_long(long_km, lat_km):
    """
    Convert a longitude distance (in kilometers) back to degrees.

    Parameters
    ----------
    long_km : float or array_like
        Longitude distance, in kilometers.
    lat_km : float or array_like
        Latitude distance, in kilometers, used to recover the latitude in
        degrees for the cosine correction.

    Returns
    -------
    float or array_like
        Equivalent distance in degrees of longitude.
    """
    latDeg = lat_km/lat_to_meter
    return (long_km/lat_to_meter) * 1/(cos(radians(latDeg)))

def calculateLong_to_meter(Lat): # determines the meters/long conversion for each input lattitude using earth's radius as a perfect sphere
    """
    Compute the meters-per-degree-longitude conversion factor at a given
    latitude, treating Earth as a perfect sphere.

    Parameters
    ----------
    Lat : float or array_like
        Latitude, in degrees.

    Returns
    -------
    float or array_like
        Kilometers per degree of longitude at that latitude.
    """
    return (pi/180) * Re * cos(radians(Lat))