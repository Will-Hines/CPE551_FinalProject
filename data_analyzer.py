"""
Creates a composite class to perform data analysis on the energy usage data from all of the appliances
"""

import math
import pandas as pd
from appliance import Appliance
class DataAnalyzer: 
    """
    Composes many Appliance objects to calculate some metrics on their energy usage data
    """

    def __init__(self):
        """
        Creates the DataAnalyzer with an empty list with which to fill in the Appliance objects
        """

        self.appliance_list = []

    def add_appliance(self, appliance):
        """
        Add an Appliance object to the appliance_list
        """

        if not isinstance(appliance, Appliance):
            raise TypeError("You must only add Appliance objects to the Data Analyzer")
        
        else: 
            self.appliance_list.append(appliance)

    def get_total_time(self):
        """
        Gets the total time each appliance was running

        Returns: a dictionary containing the name of each appliance and the total time the appliance was running
        """
        appliance_running_times = {}

        for appliance in self.appliance_list:   # loop through all appliances 
            data = appliance.energy    # get the energy data from the energy attribute
            running_times = data[data['power'] > 5]     # filter out any times where power usage is below the baseline
            total_seconds = len(running_times)          # since the data is collected by the second, counting number of lines gets total running time in second
            total_time = pd.to_timedelta(total_seconds, unit='s')       # convert number of seconds into readable time

            appliance_running_times[appliance.name] = total_time    # add the appliance's name and total time to the dictionary

        return appliance_running_times
    
    def get_rms_power(self):
        """
        Calculates the root-mean-square (RMS) Power usage

        This gives more weight to large power spikes and can give some insight into how the thermal effect of the power usage might impact the health of the appliance

        Returns: a dictionary containing the name of each appliance and the rms power usage of the appliance
        """
        rms_powers = {}

        for appliance in self.appliance_list:   # loop through all appliances
            data = appliance.energy # get the energy data from the energy attribute

            mean_squares = (data['power']**2).mean()    # calculate the mean squares
            rms_power = math.sqrt(mean_squares)     # final calculation: get the RMS power usage
            rms_powers[appliance.name] = rms_power  # add the appliance's name and the rms powers to the dictionary

        return rms_powers
    
    def get_energy_cost(self,cost_per_kwh=0.1765):      # Default cost per kwh based on the US Average
        """
        Calculates the total energy use in kwh as well as the cost (based on US Energy rates) of this energy use

        Returns: a dictionary containing the appliance name and a tuple with the total energy use in kwh and the cost of that energy in USD
        """

        kwh_and_costs = {}
        
        for appliance in self.appliance_list:   # loop through all appliances
            data = appliance.energy

            total_kwh = (appliance.get_total_energy()) / (3600 * 1000) # take the total energy (in J) then divide by 1 hour (3600 seconds) and 1000 (to convert from watt-hours to kilowatt-hours)
            total_cost = total_kwh * cost_per_kwh

            kwh_and_costs[appliance.name] = (total_kwh, total_cost)

        return kwh_and_costs
    
    