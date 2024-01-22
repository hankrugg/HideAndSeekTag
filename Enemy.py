'''
 Hank Rugg, Jan 20

 Enemy Class for Hide and Seek Tag, console based version. This class inherits from player.

'''

from Player import Player
from random import randint


class Enemy(Player):
    def __init__(self, xcoord, ycoord, ready):
        super().__init__(xcoord, ycoord, ready)

    def search(self, i, j):
        x = randint(0, 1)
        if x == 0:
            if self.xcoord <= i:
                self.xcoord += 1
            else:
                self.xcoord -= 1
        if x == 1:
            if self.ycoord <= j:
                self.ycoord += 1
            else:
                self.ycoord -= 1

