import random
from .base_player import BasePlayer
class RandomPlayer(BasePlayer):
    def __init__(self):
        self.name = "Random"
        self.hand = []

    def take_turn(self, game_state):
        print(f"{self.name}'s hand:", self.hand)
        
        # Randomly select a card to discard
        card_to_discard = random.choice(self.hand)
        self.hand.remove(card_to_discard)
        print(f"{self.name} discards:", card_to_discard)
        
        # Draw a card from the deck or discard pile
        if game_state['deck']:
            drawn_card = game_state['deck'].pop()
            self.hand.append(drawn_card)
            print(f"{self.name} draws:", drawn_card, "from the deck.")
        elif game_state['discard_pile']:
            drawn_card = game_state['discard_pile'].pop()
            self.hand.append(drawn_card)
            print(f"{self.name} draws:", drawn_card, "from the discard pile.")
        else:
            print("No cards left in the deck or discard pile.")
