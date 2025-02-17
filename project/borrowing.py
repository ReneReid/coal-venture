def display_options():
    print("1: Borrow from bank")
    print("2: Borrow from contacts")
    print("3: Borrow from loan shark")
    print("4: Display balance asset")
    print("5: Go back")


def borrow_money():
    display_options()
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        print("choice 1")
    elif choice == '2':
        print("choice 2")
    elif choice == '3':
        print("choice 3")
    elif choice == '4':
        print("choice 4")
    elif choice == '5':
        return
    else:
        print("Invalid choice. Please select a number between 1 and 5.")
