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