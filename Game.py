'''
 Hank Rugg, Jan 18

 Game Class for Hide and Seek Tag, console based version.This class controls the game.

'''

from random import randint
from Map import Map
from Player import Player


class Game:
    def __init__(self):
        self.map = Map()

    def readyGame(self):
        self.map.drawMap()

    def placePlayer(self):
        x = randint(1, 4)
        y = randint(1, 8)
        self.player = Player(x, y, False)
        while self.player.checkValidMove(x,y,self.map.array) == False:
            x = randint(1, 4)
            y = randint(1, 8)
            self.player = Player(x,y,False)

    def renderMap(self):
        self.map.resetMap()
        for i in range(5):
            for j in range(10):
                if i == self.player.xcoord and j == self.player.ycoord:
                    self.map.array[i][j] = 'O'
        self.map.drawMap()

    def makeMove(self):
        self.renderMap()
        for i in range(10):
            direction = input("Where would you like to go?")
            if self.player.checkValidMove(self.player.simulateMove(direction)[0],self.player.simulateMove(direction)[1], self.map.array):
                self.player.move(direction)
                self.renderMap()
            else:
                print("Invalid move")



if __name__ == '__main__':
    game = Game()
    game.placePlayer()
    game.makeMove()
    print("done")
