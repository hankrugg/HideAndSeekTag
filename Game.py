'''
 Hank Rugg, Jan 18

 Game Class for Hide and Seek Tag, console based version.This class controls the game.

'''

from random import randint

from Enemy import Enemy
from Map import Map
from Player import Player


class Game:
    def __init__(self):
        self.map = Map()
        self.player = None
        self.enemy = None

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
                if i == self.enemy.xcoord and j == self.enemy.ycoord:
                    self.map.array[i][j] = 'P'
        self.map.drawMap()

    def makeMove(self):
        self.renderMap()
        for i in range(10):
            direction = input("Where would you like to go?")
            if self.player.checkValidMove(self.player.simulateMove(direction)[0],self.player.simulateMove(direction)[1], self.map.array):
                self.player.move(direction)
                self.enemyMove()
                self.renderMap()
            else:
                print("Invalid move")

    def placeEnemy(self):
        x = randint(1, 4)
        y = randint(1, 8)
        self.enemy = Enemy(x, y, False)
        while self.enemy.checkValidMove(x,y,self.map.array) == False:
            x = randint(1, 4)
            y = randint(1, 8)
            self.enemy = Enemy(x,y,False)

    def enemyMove(self):
        self.enemy.search(self.player.xcoord, self.player.ycoord)




if __name__ == '__main__':
    game = Game()
    game.placePlayer()
    game.placeEnemy()
    game.makeMove()
    print("done")
