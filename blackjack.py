import os
import random
from blackjackplayers.base_player import BasePlayer
from importlib import import_module

# Load player plugins
player_folder = 'blackjackplayers'
player_files = [f[:-3] for f in os.listdir(player_folder) if f.endswith('.py') and f != 'base_player.py']

players = []
for player_file in player_files:
    module = import_module(f'{player_folder}.{player_file}')
    player_classes = [getattr(module, item) for item in dir(module) if isinstance(getattr(module, item), type)]
    for player_class in player_classes:
        if issubclass(player_class, BasePlayer) and player_class is not BasePlayer:
            players.append(player_class())

# Define your deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [(rank, suit) for suit in suits for rank in ranks]

def play_rummy(players):
    # Initialize the game
    random.shuffle(deck)
    
    # Deal cards to players
    for _ in range(7):  # Deal 7 cards each
        for player in players:
            card = deck.pop()
            player.hand.append(card)
    
    game_state = {"deck": deck, "discard_pile": []}
    
    while game_state["deck"]:    
        # Simulate player turns
        for player in players:
            print(f"{player.name}'s turn:")
            player.take_turn(game_state)  # Assuming take_turn modifies the hand
            print()


if __name__ == '__main__':
    play_rummy(players)
