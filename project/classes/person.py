import re

class Person:
    def __init__(self, name, difficulty):
        if self.is_valid_name(name):
            self.name = name
        else:
            raise ValueError("Invalid name: Name must be alphabetical character between 1 and 19 length")
        self.cash = self.set_cash(difficulty)
        self.liabilities = 0
        self.contacts = []
        self.skills = []
    


    def display_info(self):
        print(f"Name: {self.name}, Cash: {self.cash}, Liabilities: {self.liabilities}, Contacts: {self.contacts}, Skills: {self.skills}")

    def is_valid_name(self, name):
        if re.match("^[A-Za-z]{1,19}$", name):
            return True
        return False

    def is_valid_difficulty(self, difficulty):
        print("validate the difficulty level")
    
    def set_cash(self, difficulty):
        print("get a normal distribution library working here")
    
    def set_liabilities(self, difficulty):
        print("get a normal distribution library working here")

    def set_periodic_costs(self, difficulty):
        print("set periodic recurring costs")
    
    def set_periodic_income(self, difficulty):
        print("this will likely be through variety of different asset classes")
