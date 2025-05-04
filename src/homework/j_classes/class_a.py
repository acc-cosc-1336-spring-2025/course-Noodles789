import random

class die:
    def __init__(self):
        pass
    
    def roll(self):
        self.roll_value = random.randint(1, 6)
        return self.roll_value
    
    def get_rolled_value(self):
        return self.roll_value
    
    def __str__(self):
        return f"The rolled value is {self.roll_value}"