from Core.Node import Node
from pygame.locals import *
from random import randint
import math

import pygame
import json

class Maze(object):

    def __init__(self, **kwargs): #MAZe constructor
        self.step_start = ()
        self.step_end = ()
        self.solved = False
        self.__generate_random_map()

    def __generate_random_map(self):
        template = self.__get_random_template()
        #generate random start point
        i = 0; j = 0; k = 0;
        while template[i][j][k] != 'n':
            i = randint(0, self.height - 1)
            j = randint(0, self.length - 1)
            k = randint(0, self.width - 1)
        self.start_node = Node(i, j, k, self, None)
        template[i][j][k] = 'S'
        
        #generate random end point
        while template[i][j][k] != 'n':
            i = randint(0, self.height - 1)
            j = randint(0, self.length - 1)
            k = randint(0, self.width - 1)
        self.end_node = Node(i, j, k, self, None)
        template[i][j][k] = 'E'

        #generate numbers
        for i in range(0, self.height):
            for j in range(0, self.length):
                for k in range(0, self.width):
                    if template[i][j][k] == 'n':
                        template[i][j][k] = randint(1, math.ceil(min(self.width, self.length) / 2))
        self.map = template
    
    #initializes random map template to be loaded
    def __get_random_template(self):
        temp_n = randint(0,2)
        try:
            with open("Core/Template-" + str(temp_n) + ".JSON") as data_file:  
                #JSON file is found and can be loaded  
                template = json.load(data_file)
        except (FileNotFoundError, TypeError, ValueError) as e:
            #JSON file can not be found or is unreadable
            template = self.__init_template_from_air(temp_n)

        self.height = len(template)
        self.length = len(template[0])
        self.width = len(template[0][0])
        return template
            
    # default map when JSON file is not found
    def __init_template_from_air(self, n):

        template1 = [[['#', '#', '#', 'n', '#', 'n', 'n', 'n', 'n', '#', '#', '#', 'n', 'n', 'n', 'n', '#'],
                  ['#', 'n', '#', 'n', 'n', '#', 'n', 'n', 'n', 'n', 'n', '#', '#', '#', '#', 'n', '#'],
                  ['#', 'n', 'n', 'n', 'n', '#', '#', 'n', '#', 'n', '#', '#', 'n', '#', '#', 'n', '#'],
                  ['#', 'n', '#', 'n', 'n', 'n', 'n', 'n', 'n', '#', 'n', 'n', 'n', '#', '#', 'n', '#'],
                  ['#', 'n', '#', '#', 'n', '#', '#', '#', 'n', 'n', 'n', 'n', '#', 'n', '#', 'n', '#'],
                  ['#', 'n', 'n', '#', 'n', '#', '#', 'n', '#', 'n', 'n', 'n', 'n', 'n', 'n', 'n', '#'],
                  ['#', '#', '#', 'n', 'n', 'n', 'n', 'n', '#', '#', '#', '#', 'n', 'n', 'n', 'n', '#'],
                  ['#', 'n', '#', 'n', 'n', '#', 'n', '#', 'n', 'n', '#', 'n', '#', 'n', 'n', 'n', '#'],
                  ['#', 'n', 'n', 'n', '#', '#', '#', 'n', '#', 'n', 'n', 'n', '#', 'n', '#', 'n', '#']]]
                

        template2 = [[[ 'n', 'n', 'n', '#', 'n'],
                  [ '#', 'n', 'n', 'n', 'n'],
                  [ 'n', 'n', '#', '#', 'n'],
                  [ 'n', '#', 'n', 'n', 'n'],
                  [ 'n', '#', 'A', 'n', 'n']],

                 [[ 'n', 'n', 'A', 'n', 'n'],
                  [ 'n', '#', 'n', '#', '#'],
                  [ 'n', '#', 'n', 'n', 'n'],
                  [ 'n', '#', '#', '#', 'n'],
                  [ 'n', 'n', 'A', 'n', 'n']],
                
                 [[ '#', 'n', 'A', 'n', 'n'],
                  [ 'n', 'n', 'n', 'n', 'n'],
                  [ 'n', '#', '#', '#', 'n'],
                  [ 'n', 'n', 'n', '#', 'n'],
                  [ 'n', '#', 'n', '#', 'n']]]

        template3 = [[['n', '#', '#', '#', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', '#', '#', '#', '#', 'n'],
                      ['#', 'n', '#', '#', 'n', '#', '#', 'n'],
                      ['#', 'n', '#', 'n', 'n', 'n', 'n', 'n'],
                      ['#', 'n', '#', '#', 'n', '#', '#', '#'],
                      ['#', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['#', '#', '#', '#', 'n', 'n', 'n', 'n'],
                      ['#', 'n', '#', 'n', 'n', '#', 'n', 'n'],
                      ['#', 'n', 'n', 'n', '#', '#', '#', 'A']],

                     [['#', '#', '#', 'n', '#', 'n', 'n', 'n'],
                      ['#', 'n', '#', 'n', 'n', 'n', 'n', 'n'],
                      ['#', 'n', 'n', 'n', 'n', '#', '#', 'n'],
                      ['n', '#', 'n', 'n', 'n', '#', '#', 'n'],
                      ['n', 'n', 'n', 'n', '#', 'n', '#', 'n'],
                      ['#', 'n', 'n', '#', 'n', 'n', '#', 'n'],
                      ['#', 'n', '#', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', '#', 'n', '#', 'n', 'n', 'n'],
                      ['#', 'n', 'n', 'n', '#', 'n', '#', 'A']]]
        
        templates = [template1, template2, template3]
        #Saving the template to JSON file for later use
        self.__saveToFile(templates[n], n)
        return templates[n]
     
    def __saveToFile(self, template, n):
        with open('Core/Template-' + str(n) + '.JSON', 'w') as outfile:
            json.dump(template, outfile)

    #Drawing the map into the GUI
    def draw(self,display_surf,wall_surf, stairs_surf, start_surf, end_surf, floor_surf):
        tile_size = 44
        self.font = pygame.font.SysFont("monospace", 25, True)

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

                        tile_label = self.font.render(str(self.map[k][i][j]), 1, font_colour)
                        display_surf.blit(tile_label, ( (j + k * self.width + k + 1) * tile_size + 12, (i + 1) * tile_size + 12))
                        if self.solved:
                            cost_label = self.font.render(self.str, 1, (255, 255, 255)) #displaying final cost
                            display_surf.blit(cost_label, ( 10, (self.length + 4) * tile_size))
                            step_label = self.font.render("Move from " + str(self.step_start) + " to " + str(self.step_end), 1, (255, 255, 255)) #displaying the moves step by step
                            #print("Move from " + str(self.step_start) + " to " + str(self.step_end))
                            display_surf.blit(step_label, ( 10, (self.length + 5) * tile_size))
                    j = j + 1
                if k == (self.height - 1): #if last floor, print the final floor sperator
                    display_surf.blit(floor_surf,( (j + k * self.width + k + 1) * tile_size, (i + 1) * tile_size))
                i = i + 1;
        
        #bottom floor seperator
        for k in range(0, self.width * self.height + self.height + 1):
            display_surf.blit(floor_surf,( k * tile_size, (self.length + 1) * tile_size))
        guide_label = self.font.render("Press 1 for DFS, 2 for BFS, 3 for UCS", 1, (255, 255, 255))
        display_surf.blit(guide_label, ( 10, (self.length + 2) * tile_size))
        guide_label = self.font.render("Use left and right arrows to navigate through steps", 1, (255, 255, 255))
        display_surf.blit(guide_label, ( 10, (self.length + 3) * tile_size))

    def print (self, str):
        self.str = str
        print(str)

