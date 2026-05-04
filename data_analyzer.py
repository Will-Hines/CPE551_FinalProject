"""
Module to perform some statistical analysis on the energy usage data
"""

import math
import NumPy
import pandas as pd

def get_total_time(appliance):
    """
    Gets the total time an appliance was running

    Parameters: appliance: the appliance object containing the relevant energy data

    Returns: the total time an appliance was running
    """

    data = appliance.energy    # get the energy data from the energy attribute

    running_times = data[data['power'] > 5]     # filter out any times where power usage is below the baseline
    total_seconds = len(running_times)          # since the data is collected by the second, counting number of lines gets total running time in second
    total_time = pd.to_timedelta(total_seconds, unit='s')       # convert number of seconds into readable time

    return total_time

def get_rms_power(appliance):
    """
    Calculates the root-mean-square (RMS) Power usage

    This gives more weight to large power spikes and can give some insight into how the thermal effect of the power usage might impact the health of the appliance

    Parameters: appliance: the appliance object containing the relevant energy data

    Returns: the rms power usage of the appliance
    """
    data = appliance.energy # get the energy data from the energy attribute

    mean_squares = (data['power']**2).mean()    # calculate the mean squares
    rms_power = math.sqrt(mean_squares)     # final calculation: get the RMS power usage

    return rms_power

def get_energy_cost(appliance):
    """
    Calculates the total energy use in kwh as well as the cost (based on US Energy rates) of this energy use

    Paramters: appliance: the appliance object containing the relevant energy data

    Returns: a tuple containing the total energy use in kwh and the cost of that energy in USD
    """

    data = appliance.energy
    cost_per_kwh = 0.1765       # Average cost per kwh in the United States

    total_kwh = (data['power'].sum()) / (3600 * 1000)       # take the sum of the power collumn then divide by 1 hour (3600 seconds) and 1000 (to convert from watt-hours to kilowatt-hours)
    total_cost = total_kwh * cost_per_kwh

    return (total_kwh, total_cost)