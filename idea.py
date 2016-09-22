#This file is where I test out ideas before I move them over to the main.py file.

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime


data = pd.read_csv('attacks_data.csv')
# print(data.head())


# data.Date = pd.to_datetime(data.Date)
# print(data.groupby(data.Date.dt.year).size())
#564 start 
date = datetime.strptime(data.iat[2335, 1], "%Y-%m-%d")
print(date)

#death = data.iat[594, 4]

# 2002     564
# 2003     790  #1354 + 981 = 2335
# 2004     981  #2335 + 1534 = 3869
# 2005    1534  3869 + 2286 = 6155
# 2006    2286  6155 + 2658 = 8813
# 2007    2658  8813 + 2029 = 10842
# 2008    2029
# 2009    1942
# 2010    1926
# 2011    2043
# 2012    2559
# 2013    2846
# 2014    3013
# 2015    2893
# 2016    1300

# deaths =[]
# dates = []

# start = 0;
# end = 564
# year = 2002

# while start < end: 
#   date = datetime.strptime(data.iat[start, 1], "%Y-%m-%d")
#   death = data.iat[start, 4]
#   dates.append(date)
#   deaths.append(death)
#   start += 1
 
# fig = plt.figure(dpi=128, figsize=(10,6))
# plt.plot(dates, deaths, linewidth=2, c="red")
# plt.title("Terrorism Attacks during " + str(year), fontsize=24)
# plt.xlabel('Date', fontsize=16)
# fig.autofmt_xdate()
# plt.ylabel("Deaths", fontsize=16)
# plt.show()

#looking at data types: 
#print(data.dtypes) #Date is an object

#print(data.iat[3,4])
#print(data.groupby(data.Date.dt.year).size())

#print(data.Date.dt.year)




#564 values for first year
#29363  #Total values 

