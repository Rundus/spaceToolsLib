"""
test_data_processing.py

Smoke tests for the non-CDF data-processing utilities: rotation matrices,
coordinate transforms, math helpers, and colorbars. None of these require
spacepy/cdflib/the NASA CDF library, so they should always be runnable.
"""

import numpy as np
import pytest
import spaceToolsLib as stl


# --- transforms.py: rotation matrices ---

@pytest.mark.parametrize("rot_func", [stl.Rx, stl.Ry, stl.Rz, stl.R_roll, stl.R_pitch, stl.R_yaw])
def test_rotation_matrices_are_orthogonal(rot_func):
    R = rot_func(37.0)
    # A valid rotation matrix R satisfies R @ R.T == identity
    should_be_identity = R @ R.T
    assert np.allclose(should_be_identity, np.eye(3), atol=1e-10)
    # and has determinant 1 (proper rotation, no reflection)
    assert np.isclose(np.linalg.det(R), 1.0, atol=1e-10)


def test_rotation_matrix_zero_angle_is_identity():
    assert np.allclose(stl.Rx(0), np.eye(3), atol=1e-10)
    assert np.allclose(stl.Ry(0), np.eye(3), atol=1e-10)
    assert np.allclose(stl.Rz(0), np.eye(3), atol=1e-10)


def test_DCM_is_orthogonal():
    R = stl.DCM(roll=12, pitch=-5, yaw=80)
    assert np.allclose(R @ R.T, np.eye(3), atol=1e-10)


def test_GreatCircleDistance_same_point_is_zero():
    d = stl.GreatCircleDistance(lat1=40.0, lat2=40.0, long1=-90.0, long2=-90.0)
    assert d == pytest.approx(0.0, abs=1e-8)


def test_GreatCircleDistance_is_symmetric():
    d1 = stl.GreatCircleDistance(lat1=10, lat2=20, long1=0, long2=10)
    d2 = stl.GreatCircleDistance(lat1=20, lat2=10, long1=10, long2=0)
    assert d1 == pytest.approx(d2)


# --- math/chiSquare.py, math/steradian.py ---

def test_calcChiSquare_perfect_fit_is_zero():
    yData = [1, 2, 3, 4]
    fitData = [1, 2, 3, 4]
    yErr = [0.1, 0.1, 0.1, 0.1]
    fitErr = [0.1, 0.1, 0.1, 0.1]
    result = stl.calcChiSquare(yData, fitData, yErr, fitErr, nu=1)
    assert result == pytest.approx(0.0)


def test_steradian_full_sphere():
    # integrating theta over [0, pi] and phi over a full 2*pi sweep
    # should give 4*pi steradians (the full sphere)
    result = stl.steradian(theta1=0, theta2=np.pi, phi1=0, phi2=2 * np.pi)
    assert result == pytest.approx(4 * np.pi, rel=1e-6)


# --- tools/coordinates.py ---

def test_getCoordinateKeys_detects_ENU():
    data_dict = {
        'B_east': [np.array([1, 2, 3]), {}],
        'B_north': [np.array([1, 2, 3]), {}],
        'B_up': [np.array([1, 2, 3]), {}],
        'Epoch': [np.array([1, 2, 3]), {}],
    }
    coordNames, coordSetName, coordSet = stl.getCoordinateKeys(data_dict)
    assert coordSetName == 'ENU'
    assert set(coordNames) == {'B_east', 'B_north', 'B_up'}


# --- colorbars ---

def test_matlab_parula_returns_colormap():
    from matplotlib.colors import Colormap
    cmap = stl.matlab_parula_cmap()
    assert isinstance(cmap, Colormap)
