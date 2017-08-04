from pygame.locals import *
from Core import *
import sys
import pygame

class MainGUI(object):
    #window properties
    windowWidth = 1000
    windowHeight = 700
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.maze = Maze()
 
    def on_init(self):
        pygame.init()
        pygame.RESIZABLE = True
        info = pygame.display.Info()
        windowWidth = int( info.current_w * 0.5)
        windowHeight = int( info.current_h * 0.5)
        
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        self.myfont = pygame.font.SysFont("monospace", 15)
        pygame.display.set_caption('3D Maze')
        self._running = True
        #display tiles
        self._block_surf = pygame.image.load("GUI/block.png").convert()
        self._stairs_surf = pygame.image.load("GUI/stairs.png").convert()
        self._start_surf = pygame.image.load("GUI/start.png").convert()
        self._end_surf = pygame.image.load("GUI/end.png").convert()
        self._floor_surf = pygame.image.load("GUI/floor.png").convert()
 
    def on_render(self):
        #rendering display
        self._display_surf.fill((0,0,0))
        self.maze.draw(self._display_surf, self._block_surf, self._stairs_surf, self._start_surf,  self._end_surf, self._floor_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        self.on_render()
        self.search_tool = Search(self.maze.start_node, self.maze)        
        while( self._running ):
            x=0
            events = pygame.event.get()
            for event in events:
                #responding to pressing a key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self._running = False
                    if event.key == pygame.K_1: #DFS
                        self.search_tool.set_mode(1)
                    if event.key == pygame.K_2: #BFS
                        self.search_tool.set_mode(2)
                    if event.key == pygame.K_3: #UCS
                        self.search_tool.set_mode(3)
                    if event.key == pygame.K_r: #new random map
                        self.maze = Maze()
                        self.search_tool = Search(self.maze.start_node, self.maze) 
                    if event.key == pygame.K_RIGHT and self.search_tool.mode != 0: #next step
                        self.search_tool.next_step()
            self.on_render()
        self.on_cleanup()



