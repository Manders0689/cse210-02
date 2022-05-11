# object: Card
# Responsibility: To choose card and hold value.
#
# Behavior:
#   -pick a card
#
# State:
#   -card value

# class: Card
# Attributes:
#   -value: integer
#
# Method:
#   -pick_card(): None
import random

class Card:
    """A card that has a value based on the number on it.

    The responsibility of Card is to keep track of the number value.
   
    Attributes:
        value (int): The number on it.
    """
    def __init__(self): 
        """Constructs a new instance of Card
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = 0
        self.points = 0
    
        
    def pick_card(self): 
        """Generates a new random card and calculated the points for that card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 13)
        #self.points = 100 if self.hi_lo =  else -75 if 