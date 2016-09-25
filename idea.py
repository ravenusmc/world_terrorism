#This file is where I test out ideas before I move them over to the main.py file.

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime

import pycountry
from pygal.maps.world import World


data = pd.read_csv('attacks_data.csv')
# print(data.head())



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


#################################### WORK ON TERRORISM MAP HERE

#This line gets all of the columns that I want 
first_year = data[:564]
#This line will show me how many terrorist attacks occurred in each country for that year.
group = first_year.groupby(first_year.Country).size()
#This gets me the amount of countries in the group object. 
# print(len(group))

country_list = []
death_count = []


# point = group.reset_index().values[2][1]
# print(point)

count = 0

while count < len(group):
  country_value = group.reset_index().values[count][0]
  death_value = group.reset_index().values[count][1]
  country_list.append(country_value)
  death_count.append(death_value)
  count += 1



#Lines of code to convert country names to 2 letter abbreviations
countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha2

country_codes = [countries.get(country, 'Unknown code') for country in country_list]

new_countrylist = []

#I have to convert all of the country codes to lowercase-only way the wm.add method seems to work.
for country in country_codes:
  lowercase_country = country.lower()
  new_countrylist.append(lowercase_country)

country_dictionary = {}
count = 0 
while count < len(country_codes):
  country_dictionary[new_countrylist[count]] = death_count[count]
  count += 1

wm = World()
wm.title = "Terrorist Attacks in 2002"
wm.add('World', country_dictionary)
wm.render_to_file('map.svg')



#Steps to build the world map for terrorist attacks: 

#I need to get the data sets for each year-partly already have this 'idea' from building the graphs-DONE
#I need to find all the terrorist attacks in one country for that year-Done 
#I need to add together all of those terrorist attacks.  -DONE
#I need to convert the country names to two letter abbrvaiations. -Done 
#I need to create a dictionary, which will hold all of the two letter country codes and total deaths and push them into 
#The dictionary.  -DONE
#That dictionary may then be placed into the wm.add line. -DONE

### OLD 

# data.Date = pd.to_datetime(data.Date)
# print(data.groupby(data.Date.dt.year).size())
#564 start 
# date = datetime.strptime(data.iat[2335, 1], "%Y-%m-%d")
# print(date)