from Core.Node import Node
from pygame.locals import *

import pygame
import json

class Maze(object):

    def __init__(self, **kwargs):
        self.step_start = ()
        self.step_end = ()
        try:
            with open("Core/Maze.JSON") as data_file:  
                #JSON file is found and can be loaded  
                self.map = json.load(data_file)
                self.height = len(self.map)
                self.length = len(self.map[0])
                self.width = len(self.map[0][0])
        except (FileNotFoundError, TypeError, ValueError) as e:
            #JSON file can not be found or is unreadable
            self.__initMapFromAir()
        
            
    # default map when JSON file is not found
    def __initMapFromAir(self):
        self.length = 5
        self.width = 5
        self.height = 3
        self.map = [ [[ 2,  1,  'S', '#', 2],
                      ['#', 3,   1,   2,  1],
                      [ 2,  1,  '#', '#', 3],
                      [ 2, '#',  2,   3,  2],
                      [ 3, '#', 'A',  1,  1]],

                     [[ 1,  1,  'A',  1,   1],
                      [ 1, '#',  1,  '#', '#'],
                      [ 3, '#',  2,   1,   2],
                      [ 2, '#', '#', '#',  3],
                      [ 1,  3,  'A',  2,   1]],
                
                     [['#', 1,  'A',  3,  2],
                      [ 2,  3,   2,   2,  3],
                      [ 1, '#', '#', '#', 1],
                      [ 2,  1,   1,  '#', 2],
                      [ 1, '#', 'E', '#', 1]]
                   ]
        #Saving the default map to JSON file for later use
        self.__saveToFile()
    
    
    def __saveToFile(self):
        with open('Core/Maze.JSON', 'w') as outfile:
            json.dump(self.map, outfile)

    def printMaze(self):
        print(self.map)

    #Drawing the map into the GUI
    def draw(self,display_surf,wall_surf, stairs_surf, start_surf, end_surf, floor_surf):
        tile_size = 44
        font = pygame.font.SysFont("monospace", 25, True)

        #top floor seperator
        for k in range(0, self.width * self.height + self.height + 1):
            display_surf.blit(floor_surf,( k * tile_size, 0))

        for k in range(0, self.height): #repeated for number of floors
            for i in range(0, self.length): #repeated for floor length
                #displaying the floor seperator between each floor
                display_surf.blit(floor_surf,( k * tile_size * (self.width + 1) , (i + 1) * tile_size))
                for j in range(0,self.width): #repeated for floor width
                    if not(isinstance(self.map[k][i][j], int)): #if not an empty space which can be traversed
                        tile = None;
                        if self.map[k][i][j] == '#': #wall
                            tile = wall_surf
                        elif self.map[k][i][j] == 'A': #stairs
                            tile = stairs_surf
                        elif self.map[k][i][j] == 'S': #start tile
                            tile = start_surf
                            self.start_node = Node(k,i,j,self,None)
                        elif self.map[k][i][j] == 'E': #end tile
                            tile = end_surf
                        display_surf.blit(tile,( (j + k * self.width + k + 1) * tile_size, (i + 1) * tile_size))
                    else:
                        font_colour = (255, 255, 255)
                        if (k, i, j) == self.step_start:
                            font_colour = (255, 0, 0)
                        elif (k, i, j) == self.step_end:
                            font_colour = (0, 255, 0)

                        label = font.render(str(self.map[k][i][j]), 1, font_colour)
                        display_surf.blit(label, ( (j + k * self.width + k + 1) * tile_size + 12, (i + 1) * tile_size + 12))
                    j = j + 1
                if k == (self.height - 1): #if last floor, print the final floor sperator
                    display_surf.blit(floor_surf,( (j + k * self.width + k + 1) * tile_size, (i + 1) * tile_size))
                i = i + 1;
        
        #bottom floor seperator
        for k in range(0, self.width * self.height + self.height + 1):
            display_surf.blit(floor_surf,( k * tile_size, (self.length + 1) * tile_size))
