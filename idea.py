#This file is where I test out ideas before I move them over to the main.py file.

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime

import pycountry


data = pd.read_csv('attacks_data.csv')
print(data.head())

county_list = []
count = 0 

while count <= 564:
  


country = data.iat[0, 2]
print(country)


# input_countries = ['Andorra', 'United Arab Emirates', 'Afghanistan']

# countries = {}
# for country in pycountry.countries:
#     countries[country.name] = country.alpha2

# codes = [countries.get(country, 'Unknown code') for country in input_countries]

# print(codes)







### OLD 

# data.Date = pd.to_datetime(data.Date)
# print(data.groupby(data.Date.dt.year).size())
#564 start 
# date = datetime.strptime(data.iat[2335, 1], "%Y-%m-%d")
# print(date)