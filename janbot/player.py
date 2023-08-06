from hand import Hand

class Player:
    name = None
    hand = None
    score = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def set_score(self, val):
        self.score = val

    def set_hand(self, hand):
        self.hand = hand
