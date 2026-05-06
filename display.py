"""
Module to display and visualize processed energy usage data. 

Uses matpotlib and several functions to display data metrics and print suggestions for energy usage reduction and optimization. 
"""

import matplotlib.pyplot as plt 
from appliance import Appliance 

def suggest_reduction (appliances): 
    """
    Function to print suggestions for reducing energy consumption based on energy usage data and times. 

    Contains common suggestions based on basic data patterns, but also references commonly used high-energy appliances. 

    Parameters: appliances (list of Appliance): the list of Appliance objects containing processed data. 
    """
    if type(appliances) != list: 
        raise TypeError("Error: Input must be a list of Appliance objects.")
    print("Suggestions: ") 
    max_energy = appliances[0] 
    for appliance in appliances: # iterate over the appliances list and find the highest energy usage 
        if appliance.get_total_energy() > max_energy:
            max_energy = appliance 
    print("Highest power consumption appliance: ", max_energy) # print out the highest energy usage appliance 
    plot_power(max_energy) # plot the power usage for the highest energy appliance 
    print(f"Consider using the {max_energy.name} less at the shown peak usage times. ")

def plot_power (appliance): 
    """
    Function to plot the power usage over time for a single Appliance object. 

    Uses matplotlib and a line chart to plot the Appliance power usage data over time 

    Parameters: appliance (Appliance): the appliance to plot power usage for. 
    """
    if type(appliance) != Appliance: 
        raise TypeError("Error: Appliance object required to plot data.")
    if (appliance.energy.size < 10000): 
        plt.plot(appliance.energy["timestamp"], appliance.energy["power"]) 
    else: 
        resampled = appliance.energy.groupby(appliance.energy.index // 3600).mean() 
        plt.plot(resampled["timestamp"], resampled["power"]) 
    plt.title(f"Power Over Time ({appliance.name})") 
    plt.xlabel("Time (s)") 
    plt.ylabel("Power (W)") 
    plt.show() 
    
