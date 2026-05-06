import pandas as pd
import pytest
from appliance import Appliance
from data_analyzer import DataAnalyzer 

def test_average_usage():
    """
    Test function to test the dynamic average usage calculation of the Appliance class. 
    """
    df = pd.DataFrame({
        "timestamp": [1, 2, 3],
        "power": [10, 20, 30]
    })
    a = Appliance("Test", df) # create an Appliance object with the given simple data 
    assert a.average_usage == 20 # the average of [10, 20, 30] should be 20 

def test_peak_usage():
    """
    Test function to test the dynamic peak usage calculation of the Appliance class. 
    """
    df = pd.DataFrame({
        "timestamp": [1, 2, 3],
        "power": [5, 15, 10]
    })
    a = Appliance("Test", df) # create an Appliance with the given simple data 
    assert a.peak_usage == 15 # peak usage should be 15 (the highest value) 

def test_total_energy():
    """
    Test function to test the total energy calculation function for Appliance objects. 
    """
    df = pd.DataFrame({
        "timestamp": [1, 2, 3, 4, 5],
        "power": [10, 10, 20, 50, 10]
    })
    a = Appliance("Test", df) # create an Appliance with the given simple data 
    assert a.get_total_energy() == 100 # the total energy usage should be 100 J 

def test_invalid_inputs():
    """
    Test function to verify that the Appliance class rejects invalid inputs for its default attributes. 
    """
    df = pd.DataFrame({
        "timestamp": [1],
        "power": [10]
    })

    with pytest.raises(TypeError):
        Appliance(123, df) # test that a non-string name raises a TypeError 

    with pytest.raises(TypeError):
        Appliance("ValidName", "not_a_dataframe") # test that a string instead of a dataframe raises a TypeError 

def test_running_times(): 
    """
    Test function to verify behavior of the get_total_time method of the DataAnalyzer class. 
    """
    df_1 = pd.DataFrame({
        "timestamp": [1, 2, 3, 4, 5],
        "power": [1, 10, 2, 5, 20]
    })
    df_2 = pd.DataFrame({
        "timestamp": [1, 2, 3],
        "power": [10, 20, 3]
    })
    a = Appliance("Name 1", df_1) # create 2 Appliance objects with different data 
    b = Appliance("Name 2", df_2)
    analyzer = DataAnalyzer() 
    analyzer.add_appliance(a) # create a DataAnalyzer object and add the Appliances to it 
    analyzer.add_appliance(b) 
    assert analyzer.get_total_time() == {"Name 1":pd.Timedelta("00:00:02"), "Name 2":pd.Timedelta("00:00:02")} 
    # the calculated list of running times should be 2 seconds each  

