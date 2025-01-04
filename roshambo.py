import random
import os

clear = lambda: os.system('cls')
clear()

def roshambo():
    print("Welcome to Rock, Paper, Scissors!")
    print("Made by: Alex")
    print("\n1. Play Rock, Paper, Scissors")
    print("2. Exit")
    
    choice = input("\n> ")
    
    if choice == '1':
        print("Rock, Paper, Scissors")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        
        user_choice = input("\n> ")
        computer_choice = random.randint(1, 3)
        
        if user_choice == '1':
            if computer_choice == 1:
                print("It's a tie!")
            elif computer_choice == 2:
                print("You lose!")
            else:
                print("You win!")
        elif user_choice == '2':
            if computer_choice == 1:
                print("You win!")
            elif computer_choice == 2:
                print("It's a tie!")
            else:
                print("You lose!")
        elif user_choice == '3':
            if computer_choice == 1:
                print("You lose!")
            elif computer_choice == 2:
                print("You win!")
            else:
                print("It's a tie!")
        else:
            print("Invalid choice.")
    else:
        print("Exiting...")

roshambo()
