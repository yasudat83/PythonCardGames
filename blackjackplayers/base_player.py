import random
class BasePlayer:
    def __init__(self):
        self.name = "Base"
        self.hand = []

    def hit(self, game_state):
        print(f"{self.name}'s turn: Hit")
        drawn_card = game_state['deck'].pop()
        self.hand.append(drawn_card)
    
    def stand(self):
        print(f"{self.name}'s turn: Stand")
    
    def double_down(self):
        print(f"{self.name}'s turn: Double Down")
    
    def split(self):
        print(f"{self.name}'s turn: Split")
    def surrender(self):
        print(f"{self.name}'s turn: Surrender")
    
    def insurance(self):
        print(f"{self.name}'s turn: Insurance")

    def take_turn(self, game_state):
        self.hit()
