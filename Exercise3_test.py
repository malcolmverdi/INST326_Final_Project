import pytest 
import Exercise3_testing as test

def test_is_valid_sample():
    assert test.is_valid_sample (sample_quality= 0.95)
    assert not test.is_valid_sample (sample_quality= 0.94)

test_is_valid_sample()

def test_is_valid_calibration():
    assert test.is_valid_calibration (calibration_time= 5)
    assert not test.is_valid_calibration (calibration_time= 6)
