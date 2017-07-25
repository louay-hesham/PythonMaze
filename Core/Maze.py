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

    def draw(self,display_surf,wall_surf, stairs_surf, start_surf, end_surf, floor_surf):
        #top floor seperator row
        for k in range(0, self.width * self.height + self.height + 1):
            display_surf.blit(floor_surf,( k * 44, 0))

        for k in range(0, self.height):
            for i in range(0, self.length):
                display_surf.blit(floor_surf,( k * self.width * 44 + k * 44, i * 44 + 44))
                for j in range(0,self.width):
                    if not(isinstance(self.map[k][i][j], int)):
                        if self.map[k][i][j] == '#':
                            display_surf.blit(wall_surf,( j * 44 + k * self.width * 44 + (k + 1) * 44, i * 44 + 44))
                        elif self.map[k][i][j] == 'A':
                            display_surf.blit(stairs_surf,( j * 44 + k * self.width * 44 + (k + 1) * 44, i * 44 + 44))
                        elif self.map[k][i][j] == 'S':
                            display_surf.blit(start_surf,( j * 44 + k * self.width * 44 + (k + 1) * 44, i * 44 + 44))
                        elif self.map[k][i][j] == 'E':
                            display_surf.blit(end_surf,( j * 44 + k * self.width * 44 + (k + 1) * 44, i * 44 + 44))
                    j = j + 1
                if k == (self.height - 1):
                    display_surf.blit(floor_surf,( j * 44 + k * self.width * 44 + (k + 1) * 44, i * 44 + 44))
                i = i + 1;

        for k in range(0, self.width * self.height + self.height + 1):
            display_surf.blit(floor_surf,( k * 44, (self.length + 1) * 44))
