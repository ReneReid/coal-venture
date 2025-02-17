from project.classes.player import *
from borrowing import *

class Game:
    def __init__(self):
        self.turn = 0
        self.difficulty = 0
        self.player = None
        self.environment = None
    
    def start_game(self):
        print("you are starting a new game")
        self.difficulty = self.get_difficulty()
        self.player = self.player_setup(self.difficulty)
        self.environment = self.environment_setup(self.difficulty) 
        self.game_running()
    
    def get_difficulty(self):
        while True:
            try:
                difficulty = int(input("input a difficulty between 1 and 10, with 1 being easiest: "))
                if 1 <= difficulty <= 10:
                    return difficulty
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")
    

    def player_setup(self, difficulty):
        name = input("please input your player name: ")
        try:
            player = Player(name, difficulty)
            player.display_info()
            return player
        except ValueError as e:
            print(e)
    

    def environment_setup(self, difficulty):
        print("this may be deleted/ subsumed into the game running bit, prior to while loop")
    

# TODO: consolidate these options into major categories which break out in to subcategories 
    def display_options(self):
        print("1: Borrow money")
        print("1a: Raise capital")
        # print("1b: Shareholder meeting")
        print("2: Purchase")
        print("2a: Display balance sheet")
        print("2b: Apply for license")
        print("3: Sell")
        print("4: Socialize")
        print("4a: Meet with contact")
        print("5: Seek advice")
        print("5a: Gain skill")
        print("6: Go to court")
        print("7: Commit crime")
        print("8: Next turn")
        print("9: Save game")
        print("10: Exit game")
    
    def game_running(self):
        moves = 0
        while True:
            self.display_options()
            choice = input("Enter your choice (1-10): ")
            if moves == self.player.num_moves_per_turn or choice == '10':
                self.turn +=1
                self.update_player()
                moves = 0
                print("Next turn")
            if choice == '1':
                borrow_money()
            elif choice == '2':
                print("choice 2")
            elif choice == '3':
                print("choice 3")
            elif choice == '4':
                print("choice 4")
            elif choice == '5':
                print("choice 5")
            elif choice == '6':
                print("choice 6")
            elif choice == '7':
                print("choice 7")
            elif choice == '8':
                self.turn += 1
                self.update_player()
                moves = 0
                print("Next turn")
            elif choice == '9':
                print("choice 9")
            else:
                print("Invalid choice. Please select a number between 1 and 10.")
            moves += 1
    
    

    

    
    
    
        
    




