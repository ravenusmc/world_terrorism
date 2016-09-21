#All of my validation functions will be kept in this file.

def main_menu_valid(choice):
    if choice == 1 or choice == 2:
        return True 
    else:
        return False 


def quit_menu_valid(choice):
    if choice == 1 or choice == 2:
        return True
    else: 
        return False


def year_valid(year):
    print(type(year))
    year_modified = int(year)
    print(type(year_modified))
    print(year_modified)
    if year_modified >= 2002 or year_modified <= 2016:
        return True
    else: 
        return False