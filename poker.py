import os
import random
from pokerplayers.base_player import BasePlayer
from importlib import import_module

# Load player plugins
player_folder = 'pokerplayers'
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

def play_poker(players):
    # Initialize the game
    random.shuffle(deck)
    
    pot = 0
    
    # Deal two private cards to each player
    for player in players:
        player.hand = [deck.pop(), deck.pop()]
        player.bet = 0
        player.fold = False
    
    # Betting round
    for player in players:
        player.bet += 100
        player.bank -= 100
        pot += 100
    
    game_state = {"deck": deck, "pot": pot}
    
    # Simulate player turns
    for player in players:
        while not player.done:
            player.take_turn(game_state)
    
    # Showdown
    active_players = [player for player in players if not player.fold]
    best_hand = None
    winners = []
    
    for player in active_players:
        player.hand.extend(game_state['community_cards'])
        player_hand_rank = player.evaluate_hand(player.hand)
        
        if best_hand is None or player_hand_rank > best_hand:
            best_hand = player_hand_rank
            winners = [player]
        elif player_hand_rank == best_hand:
            winners.append(player)
    
    pot_split = game_state["pot"] / len(winners)
    
    for winner in winners:
        winner.bank += pot_split
    
    for player in players:
        print(f"{player.name} has {player.bank} in the bank")
        player.reset()

if __name__ == '__main__':
    original = players.copy()
    while len(players) > 1:
        play_poker(players)
        print()
        for player in players:
            if player.bank <= 0:
                players.remove(player)
                print(f"Player {player.name} is out due to lack of funds")
        input("Press Enter to Continue")
    
    print(f"{players[0].name} WINS!!!")
