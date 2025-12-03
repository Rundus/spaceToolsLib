# --- coordinates.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to put functions relating to coordinates (BUT NOT THEIR TRANSFORMS)

# VARIABLES
coordinatesSets = [['_east','_north','_up'],['_x','_y','_z'],['_e','_p','_r']]
coordinatesNames = ['ENU','RktFrm','Field_Aligned']

def getCoordinateKeys(data_dict):

    keys = [key for key in data_dict.keys()]

    coordcompNames = []
    coordSetName = []
    coordSet = []

    for i, set in enumerate(coordinatesSets):

        tempCoords = []

        for key in keys:

            for coordStr in set:
                if coordStr in key.lower():
                    tempCoords.append(key)

        if len(tempCoords) == 3:
            coordcompNames = tempCoords
            coordSetName = coordinatesNames[i]
            coordSet = coordinatesSets[i]

    return coordcompNames, coordSetName, coordSet


def ILatILong_Projection(Alt, Lat, Long, b, Zproject):
    ''' Calculates the new ILat/ILong coordinates via triangulation
    based on a normalized geomagnetic field. Neglects any effects
    due to Earth's curvature and assumes datapoints are closely spaced when converting
    between kilometers to longitude.


    Takes the rocket attitude data and normalized magnetic field as inputs.
    All inputs must be same length and are:
    [1] Rocket Altitude (in kilometres)
    [2] Rocket Latitude (in degrees)
    [3] Rocket Longitude (in degrees)
    [4] Normalized ENU 3D Magnetic Vector with [[B_East, B_North, B_Up],...] format
    [5] Projection Altitude (im kilometers)

    Outputs:
    [1] ILat (in degrees)
    [2] ILong (in degrees)
    '''

    # --- FUNCTION START ---
    from spaceToolsLib.Variables.physicsVariables import lat_to_meter
    from spaceToolsLib.Tools.conversions import long_to_meter,meter_to_long
    from numpy import array
    
    # convert lat/long to kilometers
    Lat_km = array(Lat)*lat_to_meter
    Long_km = long_to_meter(long=array(Long),lat=array(Lat))
    
    tparam = [(Zproject - Alt[i])/b[i][2] for i in range(len(Alt))]
    
    # ILat
    ILat_km = array([ (Lat_km[i] + b[i][1]*tparam[i]) for i in range(len(Lat_km))])
    ILat_deg = ILat_km/lat_to_meter
    
    # ILong
    Ilong_km = array([Long_km[i] + b[i][0]*tparam[i] for i in range(len(Long_km))]) # Calculate ILong [km] 
    ILong_deg = meter_to_long(long_km=Ilong_km,lat_km=ILat_km)
    
    return ILat_deg,ILong_deg
    
        
        
