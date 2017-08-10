from Core.Node import Node
from pygame.locals import *
from random import randint
import math

import pygame
import json

class Maze(object):

    def __init__(self, file_name):
        self.solved = False
        self.__str = ""
        if file_name != None:
            self.__load_file(file_name)
        else:
            self.__generate_random_map()

    def __load_file(self, fname):
        with open(fname) as f:
            #content = f.readlines()
            self.length, self.width = [int(x) for x in next(f).split()]
            self.height = 1
            self.map = [None] * self.height
            self.tile_color = [None] * self.height
            self.map[0] = [None] * self.length
            self.tile_color[0] = [None] * self.length
            for i in range(0, self.length):
                self.map[0][i] = [None] * self.width
                self.tile_color[0][i] = [None] * self.width
                line = next(f)
                for j in range (0, self.width):
                    self.tile_color[0][i][j] = 0
                    c = line[j] 
                    if c in '0123456789':
                        self.map[0][i][j] = int(c)
                    else:
                        self.map[0][i][j] = c
                        if c == 'S':
                            self.start_node = Node(0, i, j, self, None)
                        elif c == 'E':
                            self.end_node = Node(0, i, j, self, None)


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
        self.tile_color = [None] * self.height
        for i in range(0, self.height):
            self.tile_color[i] = [None] * self.length
            for j in range(0, self.length):
                self.tile_color[i][j] = [None] * self.width
                for k in range(0, self.width):
                    self.tile_color[i][j][k] = 0
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

    def reset_colors(self):
        for i in range(0, self.height):
            for j in range(0, self.length):
                for k in range(0, self.width):
                    self.tile_color[i][j][k] = 0

    #Drawing the map into the GUI
    def draw(self,display_surf,wall_surf, stairs_surf, start_surf, end_surf, floor_surf):
        tile_size = 27
        number_font = pygame.font.SysFont("monospace", 18, True)
        text_font = pygame.font.SysFont("monospace", 18, True)
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
                            self.end_node = Node(k,i,j,self,None)
                        display_surf.blit(tile,( (j + k * self.width + k + 1) * tile_size, (i + 1) * tile_size))
                    else:
                        if self.tile_color[k][i][j] == 0:
                            font_colour = (255, 255, 255)
                        elif self.tile_color[k][i][j] == 1:
                            font_colour = (255, 255, 0)
                        elif self.tile_color[k][i][j] == 2:
                            font_colour = (100, 100, 255)
                        elif self.tile_color[k][i][j] == 3:
                            font_colour = (255, 0, 255)

                        tile_label = number_font.render(str(self.map[k][i][j]), 1, font_colour)
                        display_surf.blit(tile_label, ( (j + k * self.width + k + 1) * tile_size + 5, (i + 1) * tile_size + 5))
                        cost_label = text_font.render(self.__str, 1, (255, 255, 255)) #displaying final cost
                        display_surf.blit(cost_label, ( 10, (self.length + 7) * tile_size))
                            
                    j = j + 1
                if k == (self.height - 1): #if last floor, print the final floor sperator
                    display_surf.blit(floor_surf,( (j + k * self.width + k + 1) * tile_size, (i + 1) * tile_size))
                i = i + 1;
        
        #bottom floor seperator
        for k in range(0, self.width * self.height + self.height + 1):
            display_surf.blit(floor_surf,( k * tile_size, (self.length + 1) * tile_size))
        guide_label = text_font.render("Press 1 for DFS, 2 for BFS, 3 for UCS,", 1, (255, 255, 255))
        display_surf.blit(guide_label, ( 10, (self.length + 2) * tile_size))
        guide_label = text_font.render("4 for A* with h = Manhattan Distance, 5 for A* with h = Euclidean distance,", 1, (255, 255, 255))
        display_surf.blit(guide_label, ( 10, (self.length + 3) * tile_size))
        guide_label = text_font.render("6 for greedy with h = Manhattan Distance, 7 for greedy with h = Euclidean distance,", 1, (255, 255, 255))
        display_surf.blit(guide_label, ( 10, (self.length + 4) * tile_size))
        guide_label = text_font.render("R to generate new map", 1, (255, 255, 255))
        display_surf.blit(guide_label, ( 10, (self.length + 5) * tile_size))
        guide_label = text_font.render("Use right arrow to navigate to next step", 1, (255, 255, 255))
        display_surf.blit(guide_label, ( 10, (self.length + 6) * tile_size))

    def print (self, str):
        self.__str = str

