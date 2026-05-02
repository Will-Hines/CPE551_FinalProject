"""
Module to display and visualize processed energy usage data. 

Uses matpotlib and several functions to display data metrics and print suggestions for energy usage reduction and optimization. 
"""

import matplotlib.pyplot as plt 

def suggest_reduction (appliances): 
    """
    Function to print suggestions for reducing energy consumption based on energy usage data and times. 

    Contains common suggestions based on basic data patterns, but also references commonly used high-energy appliances. 

    Parameters: appliances (list of Appliance): the list of Appliance objects containing processed data. 
    """
    print("Suggestions: ") 

def plot_power (appliance): 
    """
    Function to plot the power usage over time for a single Appliance object. 

    Uses matplotlib and a line chart to plot the Appliance power usage data over time 

    Parameters: appliance (Appliance): the appliance to plot power usage for. 
    """
    plt.plot(appliance.energy) 
    plt.title(f"{appliance.name} Power Over Time") 
    plt.xlabel("Time (s)") 
    plt.ylabel("Power (W)") 
