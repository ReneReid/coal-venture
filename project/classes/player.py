import re
import numpy as np
import math

# TODO: Player class should inherit from a Person class 

class Player:
    def __init__(self, name, difficulty):
        if self.is_valid_name(name):
            self.name = name
        else:
            raise ValueError("Invalid name: Name must be alphabetical character between 1 and 19 length")
        self.cash = self.set_cash(difficulty)
        self.liabilities = 0
        self.col = self.set_col(difficulty)
        # this is a credit rating variable, which will be used to determine how much money you can borrow
        self.credit_rating = 0
        # this is an overall reputation variable, which will be used to determine how people react to you
        self.reputation = 0
        self.health = 0
        # contacts --> person : relationship
        self.contacts = {}
        # skills --> skill : level of skill
        self.skills = {}
        self.num_moves_per_turn = 2
    


    def display_info(self):
        print(f"Name: {self.name}, Cash: {self.cash}, Liabilities: {self.liabilities}, Cost of Living: {self.col}, Contacts: {self.contacts}, Skills: {self.skills}")

    def is_valid_name(self, name):
        if re.match("^[A-Za-z]{1,19}$", name):
            return True
        return False

    def is_valid_difficulty(self, difficulty):
        print("validate the difficulty level")
    
    def set_cash(self, difficulty):
        val = (10 - difficulty + 1) * 25000
        cash = math.ceil(np.random.normal(val, val/3, 1))
        return cash
    
    
    def set_col(self, difficulty):
        val = (difficulty) * 1000
        col = math.ceil(np.random.normal(val, val/3, 1))
        # TODO: this should be broken out into categories, which a player can modify through decision-making
        return col
    
    
    
    def set_income(self, difficulty):
        print("this will likely be through variety of different asset classes")
    
    def update_personal_finances(self):
        print("update personal finances")
    
    def update_health(self):
        print("update health")
    
    def update_reputation(self):
        print("update reputation")
    
    def update_credit_rating(self):
        print("update credit rating")
    
    def update_contacts(self):
        print("update contacts")
    
    def update_skills(self):
        print("update skills")
    
    def update_num_moves_per_turn(self):
        print("update number of moves per turn")
    
    



    
