'''
 Hank Rugg, Jan 18

 Map Class for Hide and Seek Tag, console based version. This is the base class for the map.

'''


class Map:
    def __init__(self):
        self.array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                      ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
                      ['x', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x'],
                      ['x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
                      ['x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
                      ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

    def resetMap(self):
        self.array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                      ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
                      ['x', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x'],
                      ['x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
                      ['x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
                      ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

    def drawMap(self):
        for i in self.array:
            print(i)
