from .base_player import BasePlayer
class HitMePlayer(BasePlayer):
    def __init__(self):
        super().__init__("Sub17")

    def take_turn(self, game_state):
        if self.get_total(game_state) < 17:
            self.hit(game_state)
        else:
            self.stand(game_state)