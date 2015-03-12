__author__ = 'Joshua'

import pygame

class Block(object):
    def __init__(self, size, display):
        self.size = size
        self.display = display

        self.x = 20
        self.y = 25

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.display, (255,255,255), (self.x,self.y, 20))