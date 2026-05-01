import pandas as pd

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
        data = pd.read_csv(file_path)

    except FileNotFoundError:
        print(file_path, " was not found.")
        raise FileNotFoundError
    
    except Exception as e:
        raise Exception(f"Error loading the data: {e}")
    
    required_cols = {"timestamp", "power"}
    if not required_cols.issubset(data.columns):
        raise ValueError("Dataset missing required columns.")

    return data