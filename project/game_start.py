from classes.person import *

def start_game():
    print("you are starting a new game")
    name = input("please input your player name: ")
    print("input difficulty 1 through 5, with 1 being easiest")
    try:
        player = Person(name, difficulty)
        player.display_info()
    except ValueError as e:
        print(e)
    # name set up
    # skills set up
    # contacts - randomly created
    # asset set up
        # liquid assets - money
        # other financial assets - ownership stakes in companies
        # real-estate assets
    # liability set up
    # recurring costs
    # recurring incomes