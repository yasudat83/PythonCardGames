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

To make a bot, first import our bot base.

```python
from .cardbot import CardBot

class MyBot(CardBot):
  # Do things here

```
