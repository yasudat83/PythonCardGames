from .base_player import BasePlayer
class MikePlayer(BasePlayer):
    def __init__(self):
        super().__init__("Conf")

    def take_turn(self, game_state):
        
        confidence = 1 - ( self.get_total(game_state) / 21 )
            
        if confidence > .9:
            self.double_down(game_state)
        elif confidence > .5:
            self.hit(game_state)
        else:
            self.stand(game_state)
    