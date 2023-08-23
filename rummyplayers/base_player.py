class BasePlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, card):
        self.hand.append(card)

    def take_turn(self, game_state):
        pass  # This will be implemented by specific players
