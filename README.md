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

To make a bot, first import our bot base, then overwrite the take_turn function like this:

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

class MyBot(CardBot):
  # Do things here

```
