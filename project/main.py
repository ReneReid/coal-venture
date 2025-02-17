from game_start import *
from project.classes.game import *

def display_menu():
    print("Welcome to the Text-Based RPG Menu")
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Options")
    print("4. Quit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            #start_game()
            game = Game()
            game.start_game()
            # Code to start a new game goes here
        elif choice == '2':
            print("Loading game...")
            # Code to load a game goes here
        elif choice == '3':
            print("Opening options...")
            # Code for options menu goes here
        elif choice == '4':
            print("Quitting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
