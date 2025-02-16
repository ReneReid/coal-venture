from classes.person import *

def start_game():
    print("you are starting a new game")
    difficulty = int(input("input a difficulty between 1 and 10, with 1 being easiest: "))
    #TODO: validate that difficulty is a number betweeen 1 and 10 (inclusive)
    player = game_setup(difficulty)
    game_running(player, difficulty)
    
    # skills set up
    # contacts - randomly created
    # asset set up
        # liquid assets - money
        # other financial assets - ownership stakes in companies
        # real-estate assets
    # liability set up
    # recurring costs
    # recurring incomes

def game_setup(difficulty):
    name = input("please input your player name: ")
    try:
        player = Person(name, difficulty)
        player.display_info()
        return player
    except ValueError as e:
        print(e)
    print("this is where the game is set up")

def game_running(player, difficulty):
    while True:
        #TODO: fill this in with content
        break
    print("this is the main game loop that keeps the current game running")