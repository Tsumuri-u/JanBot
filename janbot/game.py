from wall import Wall
from hand import Hand
from player import Player

class Game:
    players = []
    wall = None
    bakaze = None # prevalent wind
    kyoku = 0 # round
    honba = 0 # bonus round
    turn = 0
    riichi = 0 # number of points, not number of bets
    rules = 0b1111 # akapai, kuitan, atozuke, hanchan (0 is tonpuusen)

    def __init__(self, rules=0b1111):
        self.wall = Wall()

    def start_game():
        pass

    def start_round():
        pass

    def init_players(playercount):
        pass

    def draw(player):
        pass
    