import os
import random
import time
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

def play_blackjack(players):
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    # Initialize the game
    random.shuffle(deck)
    
    dealer = BasePlayer("Dealer")
    pot = 0
    # Deal cards to players
    for _ in range(2):  # Deal 2 cards each
        for player in players:
            card = deck.pop()
            player.hand.append(card)
        card = deck.pop()
        dealer.hand.append(card)
    
    for player in players:
        player.bet += 100
        player.bank -= 100
        pot += 100
    
    
    game_state = {"deck": deck, "upcard": dealer.hand[0], "pot": pot}
    
    print(f"Upcard is: {game_state['upcard']}")
    
    # Simulate player turns
    for player in players:
        while not player.done:
            player.take_turn(game_state)  # Assuming take_turn modifies the hand
            player_total = player.get_total(game_state)
            
    while dealer.private_total() < 17:
        dealer.hit(game_state)
    
    winners = []
    max = 0
    
    dealer_total = dealer.private_total()
    print(f"Dealer ended with {dealer.hand}")
    print(f"{dealer.name} ended with {dealer_total} points")
    
    if dealer_total > 21:
        print("Dealer Busts")
        dealer_total = 0
    
    for player in players:
        player_total = player.get_total(game_state)
        print(f"{player.name} ended with {player.hand}")
        if player_total > 21 or player.fold:
            print(f"{player.name} is out with {player_total} points")
        elif player_total > dealer_total:
            print(f"{player.name} won with {player_total} points")
            winners.append(player)
        else:
            print(f"{player.name} ended with {player_total} points")
                
    
    if len(winners) > 0:
        pot_split = game_state["pot"]/len(winners)
    
        for winner in winners:
            winner.bank += pot_split
            
    for player in players:
        print(f"{player.name} has {player.bank} in the bank")
        player.reset()
        

if __name__ == '__main__':
    original = players.copy()
    while len(players)>1:
        play_blackjack(players)
        print()
        for player in players:
            if player.bank <=0:
                players.remove(player)
                print(f"Player {player.name} is out due to lack of funds")
            time.sleep(.5)
    
    print(f"{players[0].name} WINS!!!")
