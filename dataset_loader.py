"""
Module to load the dataset as a pandas dataframe. 
"""

import pandas as pd
from pathlib import Path
from appliance import Appliance

def get_file_names():
    """
    Gets all the file names of all csv files in the /data directory. 

    Returns: a list containing Path objects for all files within the /data directory. 
    """
    pwd_path = Path.cwd()       # Get the present working directory to build the /data directory path
    data_path = pwd_path / "data"       # checks the data folder for appliance csv data files

    file_names = [f for f in data_path.iterdir() if f.is_file() and f.suffix == '.csv']      # Use Comprehension to put all existing csv files into a list

    return file_names

def load_data(file_path : Path):
    """
    Load the appliance energy data from a csv file. 

    Parameters:
        file_path (Path): a Path object containing the path to the csv file. 

    Returns:
        Pandas dataframe with the open csv file within a file handler. 
        If it fails, returns None. 
    """

    try:
        data = pd.read_csv(file_path)   # read the data from the relevant csv

    except FileNotFoundError:
        print(file_path, " was not found.")     # throw error if the filename doesn't exist
        raise FileNotFoundError
    
    except Exception as e:
        raise Exception(f"Error loading the data: {e}")     # throw error if the data loading goes wrong
    
    required_cols = {"timestamp", "power"}          # ensure the proper format of the data
    if not required_cols.issubset(data.columns):
        raise ValueError("Dataset missing required columns.")

    data["timestamp"] = pd.to_datetime(data["timestamp"]) # convert timestamp strings to Pandas timestamps 

    print(f"Dataset {file_path.name} loaded successfully.") # print a success message after each data set, as loading can take a while 
    return data

def create_appliance_objects(file_names):
    """
    Creates an appliance object for each data file in /data

    Returns: a dictinonary of all appliance objects
    """
    appliance_dict = {}

    for path in file_names:
        name = path.stem        # name the appliance after the data file we are loading it from
        try: 
            appliance = Appliance(name, load_data(path))        # create the Appliance object with the correct name and use the load_data function to load in the data
            appliance_dict[name] = appliance            # add the new Appliance object to the dict
        except FileNotFoundError: 
            print(f"Error: {path} not found. Skipping appliance.") 
    
    return appliance_dict

if __name__ == "__main__":          # Testing stuff to make sure the file functions properly
    file_names = get_file_names()
    print(f"Files in /data: {file_names}")
    appliance_dict = create_appliance_objects(file_names) # test loading all data and creating program objects 
    print(f"Final appliance dictionary: {appliance_dict}") # print the final object dictionary 
    import display 
    display.plot_power(appliance_dict["dryer"]) # test rendering a plot for the dryer dataset (example) 

