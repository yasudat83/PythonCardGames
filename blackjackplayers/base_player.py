import random
class BasePlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.fold = False
        self.bet = 0
        self.bank = 1000

    def private_total(self):
        total = 0
        aces = 0
        for card in self.hand:
            if card[0] == 'J' or card[0] == 'Q' or card[0] == 'K':
                total += 10
            elif card[0] == 'A':
                aces += 1
            else:
                total += int(card[0])
                
        if aces > 1:
            for _ in range(aces):
                total += 1
            if total + 10 < 21:
                total += 10
        elif aces == 1 and total + 11 < 21:
            total += 11
        return total
    
    def get_total(self, game_state):
        total = 0
        aces = 0
        if game_state['upcard'][0] == 'J' or game_state['upcard'][0] == 'Q' or game_state['upcard'][0] == 'K':
            total += 10
        elif game_state['upcard'][0] == 'A':
            aces += 1
        else:
            total += int(game_state['upcard'][0])
        for card in self.hand:
            if card[0] == 'J' or card[0] == 'Q' or card[0] == 'K':
                total += 10
            elif card[0] == 'A':
                aces += 1
            else:
                total += int(card[0])
                
        if aces > 1:
            for _ in range(aces):
                total += 1
            if total + 10 < 21:
                total += 10
        elif aces == 1 and total + 11 < 21:
            total += 11
        return total

    
    def hit(self, game_state):
        print(f"{self.name}'s turn: Hit")
        drawn_card = game_state['deck'].pop()
        self.hand.append(drawn_card)
    
    def stand(self, game_state):
        print(f"{self.name}'s turn: Stand")
    
    def double_down(self, game_state):
        print(f"{self.name}'s turn: Double Down")
    
    def split(self, game_state):
        print(f"{self.name}'s turn: Split")
    def surrender(self, game_state):
        print(f"{self.name}'s turn: Surrender")
    
    def insurance(self, game_state):
        print(f"{self.name}'s turn: Insurance")

    def take_turn(self, game_state):
        self.surrender()
