# PythonCardGames
This repository is for a python card game simulator. The goal is to make a card game where users can create bots to play.
# Installation Instructions

To run this program install the requirements with
```bash
pip install -r ./requirements.txt
```

Then you can run the program with
```bash
python main.py
```

# Bot Programming

To make a bot, create a file in the blackjackplayers directory, then make a subclass of the baseplayer like this:

```python
from .base_player import BasePlayer
class HitMePlayer(BasePlayer):
    def __init__(self):
        super().__init__("Sub17")

    def take_turn(self, game_state):
        if self.get_total(game_state) < 17:
            self.hit(game_state)
        else:
            self.stand(game_state)
```

From there you can use the following functions to program your bot:

```python
self.hit(game_state) # This will have the dealer give you another card
self.stand(game_state) # This will stand, and keep your current hand
self.double_down(game_state) # This will double your bet and have the dealer give you another card
self.get_total(game_state) # This will return the current total value of your hand
```
