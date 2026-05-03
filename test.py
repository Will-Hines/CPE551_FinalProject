import pandas as pd
import pytest
from appliance import Appliance

def test_average_usage():
    df = pd.DataFrame({
        "timestamp": [1, 2, 3],
        "power": [10, 20, 30]
    })
    a = Appliance("Test", df)
    assert a.average_usage == 20

def test_peak_usage():
    df = pd.DataFrame({
        "timestamp": [1, 2, 3],
        "power": [5, 15, 10]
    })
    a = Appliance("Test", df)
    assert a.peak_usage == 15

def test_total_energy():
    df = pd.DataFrame({
        "timestamp": [1, 2],
        "power": [10, 10]
    })
    a = Appliance("Test", df)
    assert a.get_total_energy() == 20

def test_invalid_inputs():
    df = pd.DataFrame({
        "timestamp": [1],
        "power": [10]
    })

    with pytest.raises(TypeError):
        Appliance(123, df)

    with pytest.raises(TypeError):
        Appliance("ValidName", "not_a_dataframe")
