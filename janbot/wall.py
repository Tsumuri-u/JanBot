import random
from ref import *

class Wall:
    wall = []
    dead_wall = []
    dora = []
    uradora = []

    def __init__(self, roll=7, akapai=True):
        self.build_wall()
        if akapai:
            self.replace_fives()
        random.shuffle(self.wall)
        self.break_wall(roll)
        self.reveal_next_dora()

    def build_wall(self):
        for i in range(4):
            self.wall.extend(manzu)
            self.wall.extend(pinzu)
            self.wall.extend(souzu)
            self.wall.extend(honors)

    def replace_fives(self):
        self.wall.remove("5m")
        self.wall.remove("5p")
        self.wall.remove("5s")
        self.wall.extend(akapai)
    
    # This break is relative to the dealer, ie. wall[0] is the first tile on the left of the wall facing the dealer
    def break_wall(self, roll):
        break_tile = ((roll % 4) * 34) - (roll*2)
        dead_wall_end = break_tile + 14

        wall_temp = self.wall[:break_tile]
        wall_temp.extend(self.wall[dead_wall_end:])

        self.dead_wall = self.wall[break_tile:dead_wall_end]
        self.wall = wall_temp
        self.wall.reverse()

    def reveal_next_dora(self):
        self.dora.append(self.dead_wall[2*len(self.dora) + 4])
        self.uradora.append(self.dead_wall[2*len(self.uradora) + 5])
