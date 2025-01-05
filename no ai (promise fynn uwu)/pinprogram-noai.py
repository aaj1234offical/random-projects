import os
import time

def mainmenu():

    clear = lambda: os.system('cls')
    clear()

    print("Welcome to my random pin program!")
    print("Made by: alex")
    print(" ")
    print("Please select an option:")
    print("1. Enter Pin")
    print("2. Exit")
    print(" ")
    choice = input("> ")
    
    if choice == '1':
        print("Enter your pin")
        pininput = input("> ")
        if pininput == pin:
            print("Pin correct!")
            time.sleep(10)
            clear()
            exit()
        else:
            print("skill issue buddy")
            time.sleep(10)
            clear()
            mainmenu()
    
    if choice == '2':
        clear()
        exit()

print("Before we enter the program, please enter your preferred pin")
pin = input("> ")
mainmenu()