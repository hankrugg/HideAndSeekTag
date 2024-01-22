'''
 Hank Rugg, Jan 18

 Game Class for Hide and Seek Tag, console based version.This class controls the game.

'''
import sys
from random import randint

from Enemy import Enemy
from Map import Map
from Player import Player


class Game:
    def __init__(self):
        self.map = Map()
        self.player = None
        self.enemies = []
        self.isOver = False
        self.playing = True

    def readyGame(self):
        self.map.drawMap()

    def placePlayer(self):
        x = randint(1, 4)
        y = randint(1, 8)
        self.player = Player(x, y, False)
        while not self.player.checkValidMove(x, y, self.map.array):
            x = randint(1, 4)
            y = randint(1, 8)
            self.player = Player(x,y,False)
        self.renderMap()

    def renderMap(self):
        self.map.resetMap()
        for i in range(5):
            for j in range(10):
                if i == self.player.xcoord and j == self.player.ycoord:
                    self.map.array[i][j] = 'O'
                for k in range(len(self.enemies)):
                    if i == self.enemies[k].xcoord and j == self.enemies[k].ycoord:
                        self.map.array[i][j] = 'P'


    def makeMove(self):
        self.renderMap()
        self.map.drawMap()
        direction = input("Where would you like to go?")
        if direction == 'w' or direction == 's' or direction == 'd' or direction == 'a':
            if self.player.checkValidMove(self.player.simulateMove(direction)[0],
                                          self.player.simulateMove(direction)[1],
                                          self.map.array):
                self.player.move(direction)
                self.enemyMove()
                self.renderMap()
            else:
                print("Invalid move")
        else:
            print("Invalid direction")

    def placeEnemies(self):
        for i in range(3):
            x = randint(1, 4)
            y = randint(1, 8)
            if not self.player.checkValidMove(x,y,self.map.array):
                while not self.player.checkValidMove(x, y, self.map.array):
                    x = randint(1, 4)
                    y = randint(1, 8)
                self.enemies.append(Enemy(x,y,False))
                self.renderMap()
            else:
                self.enemies.append(Enemy(x,y,False))
                self.renderMap()



    def enemyMove(self):
        for enemy in self.enemies:
            direction = enemy.search(self.player.xcoord, self.player.ycoord)
            if enemy.checkValidMove(enemy.simulateMove(direction)[0],
                                          enemy.simulateMove(direction)[1],
                                          self.map.array):
                enemy.move(direction)


    def checkKill(self):
        for enemy in self.enemies:
            if enemy.xcoord == self.player.xcoord and enemy.ycoord == self.player.ycoord:
                self.isOver = True

    def playGame(self):
        self.placePlayer()
        self.placeEnemies()
        while not self.isOver:
            self.makeMove()
            self.checkKill()
        self.resetGame()
        print("___________________________________________________")
        print("Game Over!")
        print("___________________________________________________")



    def resetGame(self):
        self.isOver = False

    def showMenu(self):
        print("___________________________________________________")
        print("Welcome to Hide and Seek Tag!")
        print("Options:")
        print("1: Instructions")
        print("2: Leaderboard")
        print("3: Play")
        print("4: Quit")
        print("___________________________________________________")



    def showInstructions(self):
        print("___________________________________________________")
        print("Welcome to (virtual) Hide and Seek Tag")
        print("Controls:")
        print("w: Move up")
        print("s: Move down")
        print("a: Move right")
        print("d: Move left")
        print("The goal of the game is to last as long as you can,")
        print("there will be enemies that are trying to chase you,")
        print("your goal is to evade them for as long as you can.")
        print("___________________________________________________")


    def getChoice(self, option):
        if option == "1":
            game.showInstructions()
        elif option == "2":
            game.showLeaderboard()
        elif option == "3":
            game.playGame()
        elif option == "4":
            sys.exit()
        else:
            print("Please make a valid choice!")


    def showLeaderboard(self):
        pass


if __name__ == '__main__':
    game = Game()

    game.showMenu()
    option = input("Click the option you want and then press enter.")
    game.getChoice(option)
    while game.playing:
        game.showMenu()
        option = input("Click the option you want and then press enter.")
        game.getChoice(option)






