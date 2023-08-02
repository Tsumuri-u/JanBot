from ref import *

class Hand:
    hand = []
    opens = []
    discards = [] # every element is a pair, eg. ("1p", True) where True is tedashi and False is tsumogiri
    player_wind = ""
    yaku = 0
    fu = 0
    pei = 0

    def __init__(self):
        self.hand = []