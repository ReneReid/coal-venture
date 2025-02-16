import re
import numpy as np
import math

class Person:
    def __init__(self, name, difficulty):
        if self.is_valid_name(name):
            self.name = name
        else:
            raise ValueError("Invalid name: Name must be alphabetical character between 1 and 19 length")
        self.cash = self.set_cash(difficulty)
        self.liabilities = self.set_liabilities(difficulty)
        self.col = self.set_col(difficulty)
        self.credit_rating = 10
        self.clout = 0
        self.health = 0
        self.contacts = []
        self.skills = []
    


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
    
    def set_liabilities(self, difficulty):
        val = (difficulty) * 25000
        liab = math.ceil(np.random.normal(val, val/3, 1))
        # TODO: this should be refined to include an interest rate, or a type of liability category
        return liab

    def set_col(self, difficulty):
        val = (difficulty) * 1000
        col = math.ceil(np.random.normal(val, val/3, 1))
        # TODO: this should be broken out into categories, which a player can modify through decision-making
        return col
    
    
    
    def set_periodic_income(self, difficulty):
        print("this will likely be through variety of different asset classes")
