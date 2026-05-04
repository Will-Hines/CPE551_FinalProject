"""
Modeule to load the dataset as a pandas dataframe
"""

import pandas as pd
from pathlib import Path

def get_file_names():
    """
    Gets all the file names of all csv files in the /data directory

    Returns: a list containing the names of all files within the /data directory
    """
    folder_path = Path('./data')       # checks the data folder for appliance csv data files

    file_names = [f.name for f in folder_path.iterdir() if f.is_file() and f.suffix == '.csv']      # Use Comprehension to put all existing csv files into a list
    
    return file_names

def load_data(file_path : str):
    """
    Load the appliance energy data from a csv file

    Args:
        file_path (str): the relative path where the csv can be loacated

    Returns:
        Pandas dataframe with the open csv file within a file handler
        If it fails, returns nothing
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

    return data