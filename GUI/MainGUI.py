from pygame.locals import *
from Core import *
import sys
import pygame

class MainGUI(object):
    #window properties
    __windowWidth = 1024
    __windowHeight = 720
 
    def __init__(self):
        self.__running = True
        self.__display_surf = None
        self._image_surf = None
        self.__block_surf = None
        self.__maze = Maze(None)
 
    def __on_init(self):
        pygame.init()
        self.__display_surf = pygame.display.set_mode((self.__windowWidth,self.__windowHeight), pygame.RESIZABLE)
        pygame.display.set_caption('3D Maze')
        self.__running = True
        #display tiles
        self.__block_surf = pygame.image.load("GUI/block.png").convert()
        self.__stairs_surf = pygame.image.load("GUI/stairs.png").convert()
        self.__start_surf = pygame.image.load("GUI/start.png").convert()
        self.__end_surf = pygame.image.load("GUI/end.png").convert()
        self.__floor_surf = pygame.image.load("GUI/floor.png").convert()
 
    def __on_render(self):
        #rendering display
        self.__display_surf.fill((0,0,0))
        self.__maze.draw(self.__display_surf, self.__block_surf, self.__stairs_surf, self.__start_surf,  self.__end_surf, self.__floor_surf)
        pygame.display.flip()
 
    def __on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.__on_init() == False:
            self.__running = False
        self.__on_render()
        self.__search_tool = Search(self.__maze.start_node, self.__maze.end_node, self.__maze)        
        while( self.__running ):
            events = pygame.event.get()
            for event in events:
                #responding to pressing a key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.__running = False
                    if event.key == pygame.K_1: #DFS
                        self.__search_tool.set_mode(1)
                    if event.key == pygame.K_2: #BFS
                        self.__search_tool.set_mode(2)
                    if event.key == pygame.K_3: #UCS
                        self.__search_tool.set_mode(3)
                    if event.key == pygame.K_4:
                        self.__search_tool.set_mode(4)
                    if event.key == pygame.K_5:
                        self.__search_tool.set_mode(5)
                    if event.key == pygame.K_6:
                        self.__search_tool.set_mode(6)
                    if event.key == pygame.K_7:
                        self.__search_tool.set_mode(7)
                    if event.key == pygame.K_r: #new random map
                        self.__maze = Maze(None)
                        self.__search_tool = Search(self.__maze.start_node,self.__maze.end_node, self.__maze)
                    if event.key == pygame.K_a:
                        self.__maze = Maze("test1.txt")
                        self.__search_tool = Search(self.__maze.start_node,self.__maze.end_node, self.__maze)
                    if event.key == pygame.K_b:
                        self.__maze = Maze("test2.txt")
                        self.__search_tool = Search(self.__maze.start_node,self.__maze.end_node, self.__maze)
                    if event.key == pygame.K_c:
                        self.__maze = Maze("test3.txt")
                        self.__search_tool = Search(self.__maze.start_node,self.__maze.end_node, self.__maze)
                    if event.key == pygame.K_d:
                        self.__maze = Maze("test4.txt")
                        self.__search_tool = Search(self.__maze.start_node,self.__maze.end_node, self.__maze)
                    if event.key == pygame.K_RIGHT and self.__search_tool.mode != 0: #next step
                        self.__search_tool.next_step()
            self.__on_render()
        self.__on_cleanup()




