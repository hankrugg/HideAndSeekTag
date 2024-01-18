'''
 Hank Rugg, Jan 18

 Player Class for Hide and Seek Tag, console based version. This is the base class for players.

'''

class Player:
    def __init__(self, xcoord, ycoord, ready):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.ready = False

    def setYCoord(self, ycoord):
        self.ycoord = ycoord

    def setXCoord(self, xcoord):
        self.xcoord = xcoord

    def getYCoord(self):
        return self.ycoord

    def getXCoord(self):
        return self.xcoord

    def move(self, direction):
        if direction == "w":
            self.ycoord -= 1
        elif direction == "s":
            self.ycoord += 1
        elif direction == "a":
            self.xcoord -= 1
        elif direction == "d":
            self.xcoord += 1
        else:
            print("Invalid direction")

    def readyUp(self):
        self.ready = True

    def isReady(self):
        return self.ready



