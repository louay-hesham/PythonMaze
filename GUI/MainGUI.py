from pygame.locals import *
from Core import *
from GUI.Player import Player

import pygame

class MainGUI(object):
    #window properties
    windowWidth = 900
    windowHeight = 400
    player = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.player = Player()
        self.maze = Maze()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
 
        pygame.display.set_caption('3D Maze')
        self._running = True
        #display tiles
        self._image_surf = pygame.image.load("GUI/player.png").convert()
        self._block_surf = pygame.image.load("GUI/block.png").convert()
        self._stairs_surf = pygame.image.load("GUI/stairs.png").convert()
        self._start_surf = pygame.image.load("GUI/start.png").convert()
        self._end_surf = pygame.image.load("GUI/end.png").convert()
        self._floor_surf = pygame.image.load("GUI/floor.png").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass
 
    def on_render(self):
        #rendering display
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
        self.maze.draw(self._display_surf, self._block_surf, self._stairs_surf, self._start_surf,  self._end_surf, self._floor_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            events = pygame.event.get()
            for event in events:
                #responding to pressing a key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.moveLeft()
                    if event.key == pygame.K_RIGHT:
                        self.player.moveRight()
                    if event.key == pygame.K_UP:
                        self.player.moveUp()
                    if event.key == pygame.K_DOWN:
                        self.player.moveDown()
                    if event.key == pygame.K_ESCAPE:
                        self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()



