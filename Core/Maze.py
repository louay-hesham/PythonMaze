import json

class Maze(object):

    def __init__(self, **kwargs):
        try:
            with open("Core/Maze.JSON") as data_file:    
                self.map = json.load(data_file)
                self.height = len(self.map)
                self.length = len(self.map[0])
                self.width = len(self.map[0][0])
        except (FileNotFoundError, TypeError, ValueError) as e:
            self.__initMapFromAir()
            

    def __initMapFromAir(self):
        # default map when JSON file is not found
        self.length = 5
        self.width = 5
        self.height = 3
        self.map = [ [[ 2,  1,  'S', '#', 2],
                      ['#', 5,   1,   2,  1],
                      [ 2,  1,  '#', '#', 3],
                      [ 4, '#',  4,   5,  2],
                      [ 3, '#', 'A',  1,  1]],

                     [[ 1,  1,  'A',  1,   1],
                      [ 1, '#',  1,  '#', '#'],
                      [ 3, '#',  2,   1,   2],
                      [ 2, '#', '#', '#',  3],
                      [ 1,  3,  'A',  4,   1]],
                
                     [['#', 1,  'A',  5,  4],
                      [ 2,  5,   4,   2,  3],
                      [ 1, '#', '#', '#', 1],
                      [ 4,  1,   1,  '#', 2],
                      [ 1, '#', 'E', '#', 1]]
                   ]
        self.__saveToFile()
    
    
    def __saveToFile(self):
        with open('Core/Maze.JSON', 'w') as outfile:
            json.dump(self.map, outfile)

    def printMaze(self):
        print(self.map)
