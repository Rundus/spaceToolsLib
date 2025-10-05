# --- missionAttributes.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: Place to store the attributes specific to certain rockets

# TODO: Rewrite all this to jive with the CDF_output.py function

# --- --- --- ---
# --- IMPORTS ---
# --- --- --- ---
import numpy as np
import datetime as dt

# --- --- --- --- ---
# --- ATTRIBUTES ---
# --- --- --- --- ---

class makeRocketAttrs:
    def __init__(self, missionAttrs):
        self.globalAttributes = missionAttrs['globalAttributes']


# --- --- --- --- --- ---
# --- ACES II Mission ---
# --- --- --- --- --- ---
def EXAMPLE_mission_dicts():

    Example_attrs_dict = {
        'globalAttributes':
            {'Source_name': f'MISSIONNAM_#####>MISSIONNAM RKT ##.###',
             'Data_type': 'K0>Key Parameter',
             'PI_name': 'EXAMPLE PI',
             'Logical_source': f'missionNam_#####_',
             'Logical_file_id': f'missionNam_#####_00000000_v01',
             'Logical_source_description': 'Raw Data from the MISSIONNAMII mission organized by minorframe.150 words per minor frame.40 minor frames to a major frame.',
             'TEXT': 'Raw Data from the MISSIONNAMII mission organized by minorframe.150 words per minor frame.40 minor frames to a major frame.'
             },
    }

    example_attrs = makeRocketAttrs(Example_attrs_dict)

    return example_attrs

