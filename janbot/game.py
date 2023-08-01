from wall import Wall
from hand import Hand

class Game:
    players = []
    wall = None
    scores = []
    bakaze = None # prevalent wind
    kyoku = 0 # round
    honba = 0 # bonus round
    turn = 0
    riichi = 0 # number of points, not number of bets
    rules = 0b1111 # akapai, kuitan, atozuke, hanchan (0 is tonpuusen)

    def __init__(self, rules=0b1111):
        self.wall = Wall()