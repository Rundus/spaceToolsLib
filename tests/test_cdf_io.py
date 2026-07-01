"""
test_cdf_io.py

Round-trip tests for CDF read/write (loadDictFromFile / outputDataDict).

These require spacepy AND the NASA CDF C library to be installed and
configured (see setupFuncs/CDF_lib_path.txt) -- most environments running
`pytest` won't have that set up, so these tests skip themselves cleanly
rather than erroring out when spacepy is unavailable.
"""

import numpy as np
import pytest

spacepy = pytest.importorskip("spacepy", reason="spacepy/NASA CDF library not installed")

import spaceToolsLib as stl


def test_write_then_load_roundtrip(tmp_path):
    x_data = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
    y_data = np.array([1, 4, 9, 16, 25, 36], dtype=np.float64)

    data_dict_output = {
        'x': [x_data, {'LABLAXIS': 'x_data'}],
        'y': [y_data, {'DEPEND_0': 'x_data', 'LABLAXIS': 'y_data'}],
    }

    output_path = tmp_path / "roundtrip_test.cdf"
    stl.outputCDFdata(outputPath=str(output_path), data_dict=data_dict_output)

    assert output_path.exists()

    loaded = stl.loadDictFromFile(str(output_path))

    assert 'x' in loaded
    assert 'y' in loaded
    np.testing.assert_allclose(loaded['x'][0], x_data)
    np.testing.assert_allclose(loaded['y'][0], y_data)


def test_write_with_minimal_attributes(tmp_path):
    # spaceToolsLib should allow writing with empty attribute dicts
    # ("being minimal" -- see README)
    data_dict_output = {
        'x': [np.array([1, 2, 3, 4]), {}],
        'y': [np.array([1, 4, 9, 16]), {}],
    }

    output_path = tmp_path / "minimal_test.cdf"
    stl.outputCDFdata(outputPath=str(output_path), data_dict=data_dict_output)

    assert output_path.exists()
