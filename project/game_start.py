from classes.person import *

def start_game():
    print("you are starting a new game")
    difficulty = int(input("input a difficulty between 1 and 10, with 1 being easiest: "))
    #TODO: validate that difficulty is a number betweeen 1 and 10 (inclusive)
    player = player_setup(difficulty)
    environment = environment_setup(difficulty)
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

def player_setup(difficulty):
    name = input("please input your player name: ")
    try:
        player = Person(name, difficulty)
        player.display_info()
        return player
    except ValueError as e:
        print(e)
    print("this is where the game is set up")

def environment_setup(difficulty):
    # TODO: in this function, all the different entities that the player will interact with are set up
    # for example, the different mineral locations, NPC's, banks, insurance companies, etc. 
    print("this may be deleted/ subsumed into the game running bit, prior to while loop")

def display_options():
    print("Borrow money")
    print("Purchase")
    print("Sell")
    print("Socialize")
    print("Seek advice")
    print("Go to court")

def game_running(player, difficulty):
    turn = 0
    while True:
        #TODO: fill this in with content
        if not deduct_col(player):
            #TODO: go into personal insolvency or bankruptcy proceeding -- this is kind of like a end-game gateway
        
        
        turn += 1
        break
    print("this is the main game loop that keeps the current game running")


def deduct_col(player):
        if (player.cash >= player.col):
            player.cash -= player.col
            return True
        else:
            #TODO: should this be an exception? 
            print("you are illiquid!")
            return False