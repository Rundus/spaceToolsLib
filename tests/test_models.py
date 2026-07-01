"""
test_models.py

Smoke tests for spaceToolsLib.tools.models.

Note: CHAOS() and AlfvenSpeed() are not exercised end-to-end here since
CHAOS() depends on the bundled CHAOS/RC data files and the chaosmagpy
package. AlfvenSpeed() currently raises NotImplementedError (see
tools/models.py -- it previously called an undefined density(z)
ionospheric model, which raised a silent NameError). We test that the
NotImplementedError is now raised explicitly instead.
"""

import pytest
import spaceToolsLib as stl


def test_Bdip_mag_single_value():
    # Dipole field should be strongest at the pole (colat=0) and weaker at
    # the equator (colat=90) for a fixed altitude.
    B_pole = stl.Bdip_mag(Alt_km=0, Lat_deg=90)
    B_equator = stl.Bdip_mag(Alt_km=0, Lat_deg=0)

    assert B_pole > 0
    assert B_equator > 0
    assert B_pole > B_equator


def test_Bdip_mag_array_input():
    alts = [0, 0, 0]
    lats = [90, 45, 0]
    result = stl.Bdip_mag(alts, lats)

    assert len(result) == 3
    # field strength should decrease monotonically from pole to equator
    assert result[0] > result[1] > result[2]


def test_Bdip_mag_decreases_with_altitude():
    B_low = stl.Bdip_mag(Alt_km=0, Lat_deg=45)
    B_high = stl.Bdip_mag(Alt_km=1000, Lat_deg=45)

    assert B_high < B_low


def test_kineticTerm_simplify_true():
    # simplify=True should not touch the undefined density(z) path
    from math import sqrt
    result = stl.kineticTerm(kperp=1, z=100, simplify=True)
    assert result == pytest.approx(1 / sqrt(2))


def test_kineticTerm_simplify_false_raises():
    # simplify=False hits the undefined density(z)/IonMasses path -- this
    # should now fail loudly and explicitly rather than with a NameError.
    with pytest.raises(NotImplementedError):
        stl.kineticTerm(kperp=1, z=100, simplify=False)


def test_AlfvenSpeed_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        stl.AlfvenSpeed(z=100, lat=45, long=0, year=2020, kperp=1, simplify=True)
