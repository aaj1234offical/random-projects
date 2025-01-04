import random
import string
import os

clear = lambda: os.system('cls')
clear()

print("Welcome to the Password Generator!") # Welcome message
print("Made by: Alex")

print("\n1. Generate a password")
print("2. Exit")

choice = input("\n> ")

if choice == '1':
    length = input("Length of the password?\n> ")
    try:
        length = int(length)  # Convert the input to an integer
        print("random password: ", ''.join(random.choices(string.ascii_letters + string.digits, k=length)))
    except ValueError:
        print("Please enter a valid number for the length.")
else:
    print("Exiting...")