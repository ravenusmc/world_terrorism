#importing all libraries which will be used. 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime

from valid import *


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
    print("1. Graph of all deaths since 2002")
    choice = int(input("What is your choice? "))
    while not main_menu_valid(choice):
        print("Sorry that is not a correct selection")
        choice = int(input("What is your choice? "))
    if choice == 1:
        all_data()

#This function will plot all of the data which shows terrorism attacks since 2002 to present day.
def all_data():
    print("\033c")
    print("Please note that in order to move on, the graph window has to be closed!")
    input("Please press enter to continue ")
    data = pd.read_csv('attacks_data.csv')
    deaths =[]
    dates = []
    start = 0;
    date = "2002-01-01"
    while start < 29363: #The 29363 is the number of data points in the file.
      date = datetime.strptime(data.iat[start, 1], "%Y-%m-%d")
      death = data.iat[start, 4]
      dates.append(date)
      deaths.append(death)
      start += 1

    #The below lines are what will plot the data. 
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, deaths, linewidth=2, c="red")
    plt.title("Terrorism Attacks during 2002", fontsize=24)
    plt.xlabel('Date', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Deaths", fontsize=16)
    plt.show()
    quit_menu()


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