import random
from .base_player import BasePlayer
class RandomPlayer(BasePlayer):
    def __init__(self):
        super().__init__("Random")

    def take_turn(self, game_state):
        # Map the option name to the corresponding function
        option_to_function = {
            "hit": self.hit,
            "stand": self.stand,
            "double_down": self.double_down,
            "split": self.split,
            "surrender": self.surrender,
            "insurance": self.insurance
        }
        # List of available functions
        options = ["hit", "stand", "double_down", "split", "surrender", "insurance"]
        selected_option = random.choice(options)
        selected_function = option_to_function[selected_option]
        selected_function(game_state)

