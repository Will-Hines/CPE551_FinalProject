class Appliance: 
    """
    Class to represent a type of appliance, storing and calculating statistics about usage time and energy consumption about the appliance type. 

    Attributes: 
        name (string): The name (type) of appliance 
        energy (list): List containing all time series energy usage data points 

    Methods: 

    """

    def __init__ (self, name): 
        """
        Method to initialize default attributes for an Appliance object, including the name (type) of the appliance and the list of energy data values. 

        Parameters: 
            name (string): The name (type) of the apppliance. 
        """
        if type(name) != str: # check if the initial name attribute is a string 
            raise TypeError("Error: Appliance name must be a string.") # if it is not, raise a relevant TypeError explaining the issue 
        self.name = name # initialize the name attribute 
        self.energy = [] # initialize the energy list to an empty list 

    def __str__ (self): 
        """
        Method to return a string representation of the Appliance object containing its name (type) and basic energy usage data. 
        """
        return f"The {self.name} appliance " 
    
    