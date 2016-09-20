#All of my validation functions will be kept in this file.

def main_menu_valid(choice):
    if choice == 1:
        return True 
    else:
        return False 

def quit_menu_valid(choice):
    if choice == 1 or choice == 2:
        return True
    else: 
        return False