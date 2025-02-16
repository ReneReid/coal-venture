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
    print("1: Borrow money")
    print("2: Purchase")
    print("3: Sell")
    print("4: Socialize")
    print("5: Seek advice")
    print("6: Go to court")
    print("7: Commit crime")
    print("8: Save game")
    print("9: Exit game")

def game_running(player, difficulty):
    turn = 0
    while True:
        display_options()
        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            print("choice 1")
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
            print("choice 8")
        elif choice == '9':
            print("Exiting this game")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 7.")
        #TODO: fill this in with content
        if not deduct_col(player):
            #TODO: go into personal insolvency or bankruptcy proceeding -- this is kind of like a end-game gateway
            personal_insolvency(player)
        turn += 1
        break
    print("this is the main game loop that keeps the current game running")


def deduct_col(player):
        if (player.cash >= player.col):
            player.cash -= player.col
            if (player.cash <= player.col): 
                print("you are almost illiquid")
            return True
        else:
            #TODO: should this be an exception? 
            print("you are illiquid!")
            return False

def personal_insolvency(player):
    print("you are now in an insolvency proceeding")