import random
from .base_player import BasePlayer
class HitMePlayer(BasePlayer):
    def __init__(self):
        self.name = "HitMe"
        self.hand = []

    def take_turn(self, game_state):
        self.hit(game_state)