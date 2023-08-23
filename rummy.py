import os
from rummyplayers.base_player import BasePlayer
from importlib import import_module

# Load player plugins
player_folder = 'rummyplayers'
player_files = [f[:-3] for f in os.listdir(player_folder) if f.endswith('.py') and f != 'base_player.py']

players = []
for player_file in player_files:
    module = import_module(f'{player_folder}.{player_file}')
    player_classes = [getattr(module, item) for item in dir(module) if isinstance(getattr(module, item), type)]
    for player_class in player_classes:
        if issubclass(player_class, BasePlayer) and player_class is not BasePlayer:
            players.append(player_class("Player"))

# Simulate the game
def play_rummy(players):
    # Implement Rummy game mechanics using the players
    pass

if __name__ == '__main__':
    play_rummy(players)
