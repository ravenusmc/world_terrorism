#importing all libraries which will be used. 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime
import pycountry
from pygal.maps.world import World
from pygal.style import RotateStyle

from valid import *

### This function will be used to convert the country names to their two letter code. 
def country_name_convert(country_list):
  countries = {}
  for country in pycountry.countries:
    countries[country.name] = country.alpha2

  country_codes = [countries.get(country, 'Unknown code') for country in country_list]

  return country_codes

### Start of main program.

#This is the main function which will start the program. 
def main():
    print("\033c")
    print("------------------------")
    print("-------Welcome to-------")
    print("--World Terrorism Data--")
    print("------------------------")
    input("Press enter to continue to main menu ")
    main_menu()


#This function provides the main menu to the user. From here, they will be able to select what they want to do. 
def main_menu():
    print("\033c")
    data = pd.read_csv('attacks_data.csv')
    print("1. Graph of all deaths since 2002")
    print("2. Look at a graph for a specific year")
    print("3. Look at a Map for a specific year")
    choice = int(input("What is your choice? "))
    while not main_menu_valid(choice):
        print("Sorry that is not a correct selection")
        choice = int(input("What is your choice? "))
    if choice == 1:
        all_data(data)
    elif choice == 2:
        attacks_year(data)
    elif choice == 3: 
        svg_map(data)

#This function will plot all of the data which shows terrorism attacks since 2002 to present day. I also think that 
#I could combine this function with the yearly_graph to further modulize this program. However, for now, 
#I want to finish all of my objectives for this project. 
def all_data(data):
    print("\033c")
    print("Please note that in order to move on, the graph window has to be closed!")
    input("Please press enter to continue ")
    deaths =[] #This list will hold the deaths per day
    dates = [] #This list will hold the dates 
    start = 0; #The start variable is set to zero for the first value in the dataset
    while start < 29363: #The 29363 is the number of data points in the file.
      date = datetime.strptime(data.iat[start, 1], "%Y-%m-%d")
      death = data.iat[start, 4]
      dates.append(date)
      deaths.append(death)
      start += 1

    #The below lines are what will plot the data. 
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, deaths, linewidth=2, c="red")
    plt.title("Islamic Terrorist Attacks - 2002 - 2016", fontsize=24)
    plt.xlabel('Date', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Deaths", fontsize=16)
    plt.show()
    quit_menu()

#This function will allow the user to select which year they want to look at and then that information will eventually
#be used to build a graph for that specific year.
def attacks_year(data):
    print("\033c")
    print("Year: " + str(2002))
    print("Year: " + str(2003))
    print("Year: " + str(2004))
    print("Year: " + str(2005))
    print("Year: " + str(2006))
    print("Year: " + str(2007))
    print("Year: " + str(2008))
    print("Year: " + str(2009))
    print("Year: " + str(2010))
    print("Year: " + str(2011))
    print("Year: " + str(2012))
    print("Year: " + str(2013))
    print("Year: " + str(2014))
    print("Year: " + str(2015))
    print("Year: " + str(2016))
    year = int(input("Please enter the year you want to look at: "))
    while not year_valid(year):
        print("That is not an acceptable year!")
        year = int(input("Please enter the year you want to look at: "))
    start_end = year_info(year)
    yearly_graph(data, year, start_end)

#This function will take the year that the user enters and gets the first and last data point for that year 
# and then returns an array with those two values.
def year_info(year):
    start_end = []
    if year == 2002:
        start_end.append(0)
        start_end.append(564)
        return start_end
    elif year == 2003:
        start_end.append(565)
        start_end.append(1354)
        return start_end
    elif year == 2004:
        start_end.append(1354)
        start_end.append(2335)
        return start_end
    elif year == 2005:
        start_end.append(2335)
        start_end.append(3869)
        return start_end
    elif year == 2006:
        start_end.append(3869)
        start_end.append(6155)
        return start_end
    elif year == 2007:
        start_end.append(6155)
        start_end.append(8813)
        return start_end
    elif year == 2008:
        start_end.append(8813)
        start_end.append(10842)
        return start_end
    elif year == 2009:
        start_end.append(10842)
        start_end.append(12784)
        return start_end
    elif year == 2010:
        start_end.append(12784)
        start_end.append(14710)
        return start_end
    elif year == 2011:
        start_end.append(14710)
        start_end.append(16753)
        return start_end
    elif year == 2012:
        start_end.append(16753)
        start_end.append(19312)
        return start_end
    elif year == 2013:
        start_end.append(19312)
        start_end.append(22158)
        return start_end
    elif year == 2014:
        start_end.append(22158)
        start_end.append(25171)
        return start_end
    elif year == 2015:
        start_end.append(25171)
        start_end.append(28064)
        return start_end
    elif year == 2016:
        start_end.append(28064)
        start_end.append(29364)
        return start_end

#This function is what will build the graph for each individual year. 
def yearly_graph(data, year, start_end):
    print("\033c")
    print("Please note that in order to move on, the graph window has to be closed!")
    input("Please press enter to continue ")
    deaths =[]
    dates = []
    start = start_end[0]
    end = start_end[1]

    while start < end: 
      date = datetime.strptime(data.iat[start, 1], "%Y-%m-%d")
      death = data.iat[start, 4]
      dates.append(date)
      deaths.append(death)
      start += 1
     
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, deaths, linewidth=2, c="red")
    plt.title("Terrorism Attacks During " + str(year), fontsize=24)
    plt.xlabel('Date', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Deaths", fontsize=16)
    plt.show()
    quit_menu()

#This function will plot the data for a specific year to an SVG map. 
def svg_map(data):
    print("\033c")
    print("Year: " + str(2002))
    print("Year: " + str(2003))
    print("Year: " + str(2004))
    print("Year: " + str(2005))
    print("Year: " + str(2006))
    print("Year: " + str(2007))
    print("Year: " + str(2008))
    print("Year: " + str(2009))
    print("Year: " + str(2010))
    print("Year: " + str(2011))
    print("Year: " + str(2012))
    print("Year: " + str(2013))
    print("Year: " + str(2014))
    print("Year: " + str(2015))
    print("Year: " + str(2016))
    year = int(input("Please enter the year you want to look at: "))
    while not year_valid(year):
        print("That is not an acceptable year!")
        year = int(input("Please enter the year you want to look at: "))
    start_end = year_info(year)
    create_svg_map(data, start_end, year)


def create_svg_map(data, start_end, year):
    #This line gets all of the columns that I want. There are 564 data points in the first year so that is why
    #I use that number 
    year_examined = data[start_end[0]:start_end[1]]
    #This line will show me how many terrorist attacks occurred in each country for that year.
    group = year_examined.groupby(year_examined.Country).size()
    #I create two lists which will hold the countrys and the amount of people killed for that year in that country.
    country_list = []
    death_count = []
    count = 0
    #I create a while loop that will find a country and push it into the country_list list and the attacks for that 
    #country, in that specific year, into another list. 
    while count < len(group):
        country_value = group.reset_index().values[count][0]
        death_value = group.reset_index().values[count][1]
        country_list.append(country_value)
        death_count.append(death_value)
        count += 1
    #Lines of code to convert country names to 2 letter abbreviations
    country_codes = country_name_convert(country_list)
    #Another list is created to hold all of the country abbreviations which have been converted to lowercase.
    new_countrylist = []
    #I have to convert all of the country codes to lowercase-only way the wm.add method seems to work.
    for country in country_codes:
        lowercase_country = country.lower()
        new_countrylist.append(lowercase_country)
    #The wm.add method needs a dictionary to work with. Here, I create a dictionary which holds the country abbrevation
    #and the amount of terrorist attacks, for that year, in that country as the value for that key. 
    country_dictionary = {}
    count = 0 
    while count < len(country_codes):
        country_dictionary[new_countrylist[count]] = death_count[count]
        count += 1
    #These lines of code will break the attacks up into groups of 50. This, if a state has 0-50 attacks in a year
    #it will be placed into one group. Another state that has 51-100 attacks will be placed into another 
    #group. Then, when the map comes up, the user will see the attacks based on a color code. 
    attack_1, attack_2, attack_3, attack_4, attack_5, attack_6 = {}, {}, {}, {}, {}, {}
    for country, attack_count in country_dictionary.items():
        if attack_count <= 50:
            attack_1[country] = attack_count
        elif attack_count > 50 and attack_count <= 100:
            attack_2[country] = attack_count
        elif attack_count > 100 and attack_count <= 150:
            attack_3[country] = attack_count
        elif attack_count > 150 and attack_count <= 200:
            attack_4[country] = attack_count
        elif attack_count > 200 and attack_count <= 250:
            attack_5[country] = attack_count
        else:
            attack_6[country] = attack_count

    #These lines use pygal to create the map which will be a svg document.
    wm_style = RotateStyle('#336699')
    wm = World(style=wm_style)
    wm.title = "Terrorist Attacks in " + str(year)
    wm.add('0-50', attack_1)
    wm.add('51-100', attack_2)
    wm.add('101-150', attack_3)
    wm.add('151-200', attack_4)
    wm.add('201-250', attack_5)
    wm.add('>250', attack_6)
    wm.render_to_file('map.svg')


#### Non Critical Functions here 
#This function is what will allow the user to quit or go back to main menu.
def quit_menu():
    print("1. Main Menu")
    print("2. Quit")
    choice = int(input("What is your choice? "))
    while not quit_menu_valid(choice):
        print("That is not a valid option")
        choice = int(input("What is your choice? "))
    if choice == 1:
        main_menu()
    elif choice == 2:
        print("Sorry to see you leave!")
        print("Have a great day!")


main()