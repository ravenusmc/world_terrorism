#This file is where I test out ideas before I move them over to the main.py file.

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime

import pycountry
from pygal.maps.world import World


data = pd.read_csv('attacks_data.csv')
print(data.head())


# country_list = []
# death_list = []
# count = 0 

# while count <= 564:
#   country = data.iat[count, 2]
#   death_count = data.iat[count, 4]
#   country_list.append(country)
#   death_list.append(death_count)
#   count += 1

# #Lines of code to convert country names to 2 letter abbreviations
# countries = {}
# for country in pycountry.countries:
#     countries[country.name] = country.alpha2

# codes = [countries.get(country, 'Unknown code') for country in country_list]

# wm = World()
# wm.title = "World Map"
# wm.add('World', {'us': 34500993, 'fr': 334544})
# wm.render_to_file('map.svg')






#Steps to build the world map for terrorist attacks: 

#I need to get the data sets for each year-partly already have this 'idea' from building the graphs-DONE
#I need to find all the terrorist attacks in one country for that year-Done 
#I need to add together all of those terrorist attacks.  -DONE
#I need to convert the country names to two letter abbrvaiations. -Done 
#I need to create a dictionary, which will hold all of the two letter country codes and total deaths and push them into 
#The dictionary.  -DONE
#That dictionary may then be placed into the wm.add line. -DONE

### OLD 

# point = group.reset_index().values[2][1]
# print(point)


# data.Date = pd.to_datetime(data.Date)
# print(data.groupby(data.Date.dt.year).size())
#564 start 
# date = datetime.strptime(data.iat[2335, 1], "%Y-%m-%d")
# print(date)