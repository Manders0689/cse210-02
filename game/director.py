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