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
    """
    Thin wrapper that exposes a mission attributes dictionary's
    'globalAttributes' entry as an object attribute, for use as the
    default globalAttrsMod in CDF_output.outputDataDict().
    """
    def __init__(self, missionAttrs):
        """
        Parameters
        ----------
        missionAttrs : dict
            A dictionary with at least a 'globalAttributes' key, whose
            value is itself a dict of CDF global attribute name/value
            pairs.
        """
        self.globalAttributes = missionAttrs['globalAttributes']


# --- --- --- --- --- ---
# --- ACES II Mission ---
# --- --- --- --- --- ---
def EXAMPLE_mission_dicts():
    """
    Build an example/template makeRocketAttrs object with placeholder CDF
    global attributes, used as the default globalAttrsMod in
    CDF_output.outputDataDict() when the caller doesn't supply their own.

    Returns
    -------
    makeRocketAttrs
        Object whose .globalAttributes dict contains placeholder/template
        CDF global attribute values (Data_type, PI_name, Logical_file_id,
        etc.) meant to be overridden by the caller.
    """

    Example_attrs_dict = {
        'globalAttributes':
            {
            # 'Source_name': f'MISSIONNAM_#####>MISSIONNAM RKT ##.###',
             'Data_type': 'K0>Key Parameter',
             'PI_name': 'EXAMPLE PI',
             # 'Logical_source': None,
             'Logical_file_id': f'missionNam_#####_00000000_v01',
             'Logical_source_description': 'Raw Data from the MISSIONNAMII mission organized by minorframe.150 words per minor frame.40 minor frames to a major frame.',
             'TEXT': 'Raw Data from the MISSIONNAMII mission organized by minorframe.150 words per minor frame.40 minor frames to a major frame.'
             },
    }

    example_attrs = makeRocketAttrs(Example_attrs_dict)

    return example_attrs

