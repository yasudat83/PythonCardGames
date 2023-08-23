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

def play_blackjack(players):
    # Initialize the game
    random.shuffle(deck)
    
    dealer = BasePlayer()
    
    # Deal cards to players
    for _ in range(2):  # Deal 2 cards each
        for player in players:
            card = deck.pop()
            player.hand.append(card)
        card = deck.pop()
        dealer.hand.append(card)
    
    game_state = {"deck": deck, "upcard": dealer.hand[0]}
    
    print(f"Upcard is: {game_state['upcard']}")
    
    # Simulate player turns
    for player in players:
        print(f"{player.name}'s Turn")
        player.take_turn(game_state)  # Assuming take_turn modifies the hand
        player_total = player.get_total(game_state)
        print(f"{player.name} ended with {player.hand}")
        if player_total > 21:
            print(f"{player.name} Busted with {player_total} points")
        else:
            print(f"{player.name} ended with {player_total} points")
            
    winner = None
    max = 0
    
    dealer_total = dealer.get_total(game_state)
    
    if dealer_total > 21:
        print("Dealer Busts, everyone Wins")
        exit()
    else:
        winner = dealer
        max = dealer_total
    
    for player in players:
        if player.get_total(game_state) > 21:
            pass
        else:
            if player.get_total(game_state) > max:
                max = player.get_total(game_state)
                winner = player
    
    if winner is None:
        print("No one wins")
    else:
        print(f"Winner is {winner.name} with {max} points")


if __name__ == '__main__':
    play_blackjack(players)
