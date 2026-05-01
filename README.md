# Smart Energy Consumption Analyzer for Residential Homes
## Authors:
### Danielle Bonk, dbonk@stevens.edu, 20013551
### William Hines, whines@stevens.edu, 10479063
### Jason Rizzo, jrizzo1@stevens.edu, 20014637

## Project Goal and Description:
   Many households use more electricity than necessary because most people lack insight into their energy consumption patterns. Without a clear understanding of usage habits, it is difficult to identify waste or reduce consumption. This leads to higher electricity bills and increased carbon emissions, which harm the environment and further drive up electricity prices, which are already rising rapidly.   
   This project aims to develop a Python-based Smart Energy Consumption Analyzer to help users visualize how they use electricity at home. The program will analyze patterns in electricity consumption to identify peak usage times, detect abnormal energy spikes, and determine which appliances contribute the most to overall household energy usage. By comparing information from multiple households, the analyzer will give a bigger-picture view of household energy habits.    
   The program will use a publicly available dataset analyze general usage trends, with smart meter and appliance-level household electricity data providing more specific user information to load, process, and analyze energy usage. It will generate visualizations to illustrate consumption trends and highlight key findings, and present simple recommendations to users about changes in electricity usage habits that could be made to increase energy efficiency. The program should be simple for the user and easy to interact with, and provide clear and concise output. The project demonstrates how data analysis and Python programming can enhance understanding and improvement of household energy efficiency.   

## Dependencies:
pandas  
numpy  
pytest  
os  
math  

## File Structure

-- main.ipynb (runs the program + testing)  
-- appliance.py ( Creates the class object to store appliance data and such)  
-- data_analyzer.py (object that has a list of appliance objects to get a bigger picture of things)  
-- dataset_load.py (load the dataset and handle exceptions and related issues)   
-- display.py (class to generate visualizations and suggest changes in usage patterns)  
-- tests.py (all PyTest testing)
-- data (contains all csv files with data from various appliances)  
-- -- all the data files will be contained here
-- README.md (documentation)

## How to Run the Program

## Main Contributions of Each Team Member  
### Danielle
Wrote the main file and handled the writing of all tests  
### Will
Wrote data_analyzer  
### Jason
Wrote appliance.py  
