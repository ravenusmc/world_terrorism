#All of my validation functions will be kept in this file.

def main_menu_valid(choice):
    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        return True 
    else:
        return False 


def quit_menu_valid(choice):
    if choice == 1 or choice == 2:
        return True
    else: 
        return False


def year_valid(year):
    if year >= 2002 and year <= 2016:
        return True
    else: 
        return False