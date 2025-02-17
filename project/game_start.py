# from classes.person import *
# from borrowing import *

# turn = 0

# def start_game():
#     print("you are starting a new game")
#     difficulty = int(input("input a difficulty between 1 and 10, with 1 being easiest: "))
#     #TODO: validate that difficulty is a number betweeen 1 and 10 (inclusive)
#     player = player_setup(difficulty)
#     environment = environment_setup(difficulty)
#     game_running(player, difficulty)
    
#     # skills set up
#     # contacts - randomly created
#     # asset set up
#         # liquid assets - money
#         # other financial assets - ownership stakes in companies
#         # real-estate assets
#     # liability set up
#     # recurring costs
#     # recurring incomes

# def player_setup(difficulty):
#     name = input("please input your player name: ")
#     try:
#         player = Person(name, difficulty)
#         player.display_info()
#         return player
#     except ValueError as e:
#         print(e)
#     print("this is where the game is set up")

# def environment_setup(difficulty):
#     # TODO: in this function, all the different entities that the player will interact with are set up
#     # for example, the different mineral locations, NPC's, banks, insurance companies, etc. 
#     print("this may be deleted/ subsumed into the game running bit, prior to while loop")

# def display_options():
#     print("1: Borrow money")
#     print("1a: Raise capital")
#     # print("1b: Shareholder meeting")
#     print("2: Purchase")
#     print("2a: Display balance sheet")
#     print("3: Sell")
#     print("4: Socialize")
#     print("4a: Meet with contact")
#     print("5: Seek advice")
#     print("6: Go to court")
#     print("7: Commit crime")
#     print("8: Next turn")
#     print("9: Save game")
#     print("10: Exit game")

# def game_running(player, difficulty):
#     while True:
#         display_options()
#         choice = input("Enter your choice (1-10): ")
#         if choice == '1':
#             borrow_money()
#         elif choice == '2':
#             print("choice 2")
#         elif choice == '3':
#             print("choice 3")
#         elif choice == '4':
#             print("choice 4")
#         elif choice == '5':
#             print("choice 5")
#         elif choice == '6':
#             print("choice 6")
#         elif choice == '7':
#             print("choice 7")
#         elif choice == '8':
#             turn += 1
#             update_player(player)
#             print("Next turn")
#         elif choice == '9':
#             print("choice 9")
#         elif choice == '10':
#             print("Exiting this game")
#             break
#         else:
#             print("Invalid choice. Please select a number between 1 and 7.")
#         #TODO: fill this in with content
#         if not deduct_col(player):
#             #TODO: go into personal insolvency or bankruptcy proceeding -- this is kind of like a end-game gateway
#             personal_insolvency(player)
#         break
#     print("this is the main game loop that keeps the current game running")


# def deduct_col(player):
#         if (player.cash >= player.col):
#             player.cash -= player.col
#             if (player.cash <= player.col): 
#                 print("you are almost illiquid")
#             return True
#         else:
#             #TODO: should this be an exception? 
#             print("you are illiquid!")
#             return False


# def update_game():
#     # update player
#     # update other entities/ environment
#     print("update everything")

# def collect_income(player):
#     print("function to increase personal income")

# def update_health(player):
#     print("operations for updating health")


# def personal_insolvency(player):
#     print("you are now in an insolvency proceeding")


# def update_player(player):
#     deduct_col(player)
#     collect_income(player)
