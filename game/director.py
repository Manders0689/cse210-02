# object: Director
# Responsibility: controls the action in the game of picking and evaluating cards and their score.
#
# Behaviors:
#   -start Hilo game
#   -guess whether card is higher or lower from previous card
#   -picks card and calculates score
#   -shows card and score
#   -gets answer to play again
#
# State:
#   -first card
#   -second card
#   -user guess of high or low
#   -score
#   -total score
#   -user input for whether they will continue playing

# class: Director
# Attributes:
#   -card1: integer<Card>
#   -card2: integer<Card>
#   -hi_lo: boolean or string
#   -score: integer
#   -total_score: integer
#   -is_playing: boolean
#
# Methods:
#   -start_game(): None
#   -guess_hl(): None
#   -do_updates(): None
#   -do_outputs(): None
#   -get_inputs(): None

from game.card import Card
class Director: 
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card1: integer<Card>
        card2: integer<Card>
        hi_lo: boolean or string
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """
    def __init__(self): 
        """
        """
    

    def start_game(self): 
        """
        """
    

    def guess_hl(self): 
        """ Gets players guess on whether the next card is higher or lower.
        
        Args:
            self (Director): An instance of Director.
        """
        self.card1 = self.card1.pick_card()

        print(f"The card is: {self.card1}")
        self.hi_lo = input("Higher or lower? [h/l] ")

    def do_updates(self): 
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        self.card2 = self.card2.pick_card()
        
        if self.hi_lo == "h":
            if self.card2 > self.card1:
                self.score = 100 
            elif self.card2 < self.card1:
                self.score = -75
        elif self.hi_lo == "l":
            if self.card2 < self.card1:
                self.score = 100
            elif self.card2 > self.card1:
                self.score = -75
        self.total_score += self.score

    def do_outputs(self): 
        """
        """
    

    def get_inputs(self): 
        """
        """