from ref import *

class Hand:
    hand = []
    open = []
    closed = []
    discards = [] # every element is a pair, eg. ("1p", True) where True is tedashi and False is tsumogiri
    player_wind = ""
    riichi = 0
    furiten = 0
    yaku = 0
    fu = 0
    pei = 0

    def __init__(self):
        self.hand = []

    # requires tile to be a list of tiles
    def draw_tile(self, tile):
        self.hand.extend(tile)

    def discard_tile(self, tile):
        self.update_closed()
        if isinstance(tile, int):
            removed = self.closed[tile]
            self.hand.remove(removed)
            self.discards.append(removed)
            return removed
        else:
            if tile in self.closed:
                self.hand.remove(tile)
                self.discards.append(tile)
            return tile
        
    def declare_kan(self, tile):
        pass

    def declare_pon(self, tile):
        pass

    def declare_chi(self, tile):
        pass

    def declare_pei(self):
        pass

    def declare_riichi(self, tile):
        pass

    def draw_dead_wall(self, tile):
        pass
    
    # only use values in hand and open, ensure duplicates don't all get removed
    def update_closed(self):
        pass

    def set_player_wind(self, wind):
        self.player_wind = wind

