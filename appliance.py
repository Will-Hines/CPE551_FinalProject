import pandas as pd 

class Appliance: 
    """
    Class to represent a type of appliance, storing and calculating statistics about usage time and energy consumption about the appliance type. 

    Attributes: 
        name (string): The name (type) of appliance 
        energy (pandas dataframe): List containing all time series energy usage data points 
        peak_usage: The maximum power value in the energy dataframe 
        average_usage: The average (mean) power value in the energy dataframe 
    """

    def __init__ (self, name, energy): 
        """
        Method to initialize default attributes for an Appliance object, including the name (type) of the appliance and the list of energy data values. 

        Parameters: 
            name (string): The name (type) of the apppliance. 
            energy (pandas dataframe): The dataframe containing the appliance's time-series energy usage data. 
        """
        if type(name) != str: # check if the initial name attribute is a string 
            raise TypeError("Error: Appliance name must be a string.") # if it is not, raise a relevant TypeError explaining the issue 
        if type(energy) != pd.DataFrame: # check if the initial energy attribute is a dataframe 
            raise TypeError("Error: Appliance energy usage must be a Pandas DataFrame.") # if it is not, raise a relevant TypeError 
        # check for correct columns in the energy dataframe 
        if not {"timestamp", "power"}.issubset(energy.columns):
            raise ValueError("Dataset missing required columns.")
        self.name = name # initialize the name attribute 
        self.energy = energy # initialize the energy dataframe 

    def __str__ (self): 
        """
        Method to return a string representation of the Appliance object containing its name (type) and basic energy usage data. 
        """
        return f"The {self.name} appliance uses {self.average_usage} W of power on average and {self.peak_usage} W maximum." # return an f-string containing the appliance name and basic usage data 
    
    def __getattr__ (self, attr): 
        """
        Method to get attributes from the Appliance object. 

        Overrided to dynamically calculate data metrics when a dynamic attribute is referenced. 

        Parameters: attr (string): the attribute to be referenced 

        Returns: The value of the requested attribute. 
        """
        if attr == "peak_usage": # if the peak_usage attribute is requested 
            return self.energy["power"].max() # return the maximum value of the power column of the energy dataframe 
        if attr == "average_usage": # if the average_usage attribute is requested 
            return self.energy["power"].mean() # return the mean value of the power column 
        raise AttributeError(f"Error: No attribute with given name '{attr}' found.") # default case, if the attribute is not valid, raise a relevant AttributeError 
    
    def get_total_energy (self): 
        """
        Method to calculate and return the total energy usage of the Appliance from the energy dataframe. 

        Returns: (float): Total energy usage over the measurement period for the given appliance (in J). 
        """
        return self.energy["power"].size * self.average_usage # returns the average power usage multiplied by the number of seconds (data points) to get energy in J 
    
    