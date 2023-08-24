from .base_player import BasePlayer
class HitMePlayer(BasePlayer):
    def __init__(self):
        super().__init__("HitMe")

    def take_turn(self, game_state):
        self.hit(game_state)