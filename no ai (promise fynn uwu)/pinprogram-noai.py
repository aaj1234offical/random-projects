import os

def mainmenu():

    clear = lambda: os.system('cls')
    clear()

    print("Welcome to my random pin program!")
    print("Made by: alex")
    print(" ")
    print("Please select an option:")
    print("1. Set Pin")
    print("2. Enter Pin")
    print("3. Exit")
    print(" ")
    choice = input("> ")

mainmenu()

if choice == '1':
    print("Enter a new pin!")
    pin = input("Enter your new pin!")
    print("Alright!")
    mainmenu()