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