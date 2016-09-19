#This file is where I test out ideas before I move them over to the main.py file.

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime

#Get data that shows all the terrorism attacks since 2002.

data = pd.read_csv('attacks_data.csv')
# print(data.head())

#looking at data types: 
#print(data.dtypes) #Date is an object

print(data.iat[3,4])

deaths =[]
dates = []
start = 0;
date = "2002-01-01"
while start < 564: 
  date = datetime.strptime(data.iat[start, 1], "%Y-%m-%d")
  #date = data.iat[start, 1]
  death = data.iat[start, 4]
  dates.append(date)
  deaths.append(death)
  start += 1

print(deaths)

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, deaths, linewidth=2, c="red")
plt.title("Terrorism Attacks during 2002", fontsize=24)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Deaths", fontsize=16)
plt.show()







#### OLD 

#date = datetime.strptime(data.iat[start, 1], "%Y-%m-%d")
#print(data.head())

#print(data[data.Country == 'India'])
#print(data[data.Date == "2002-01-02"])

# startdate = "2002-01-02"
#print(data['Date']) + timedelta(days=1)

# newDate = pd.to_datetime(startdate) + pd.DateOffset(days=1)
#print(data[data.Date == str(newDate)])