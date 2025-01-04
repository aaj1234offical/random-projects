import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Initialize pin variable
stored_pin = None

while True:
    clear_screen()
    print("Example Pin Program")
    print("Made by: Alex")
    print(" ")
    print("Please select an option:")
    print("1. Set Pin")
    print("2. Enter Pin")
    print("3. Exit")
    print(" ")
    choice = input("> ")

    if choice == '1':
        print("Enter a new pin:")
        new_pin = input("> ")
        if new_pin.isdigit():
            stored_pin = new_pin
            print("Pin set successfully!")
        else:
            print("Invalid pin! Please use numbers only.")
        input("Press Enter to continue...")

    elif choice == '2':
        if stored_pin is None:
            print("Please set a pin first!")
        else:
            print("Enter your pin:")
            pin_input = input("> ")
            if pin_input == stored_pin:
                print("Pin correct!")
            else:
                print("Pin incorrect!")
        input("Press Enter to continue...")

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid option! Please try again.")
        input("Press Enter to continue...")