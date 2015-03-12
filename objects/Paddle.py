__author__ = 'Joshua'

import pygame

class Paddle(object):
    def __init__(self, height, width, x, display):
        self.height = height
        self.width = width
        self.display = display

        self.x = x
        self.y = 350

    def update(self):
        self.x = pygame.mouse.get_pos()[0]

    def draw(self):
        pygame.draw.rect(self.display, (255,255,255), (self.x,self.y,self.height,self.width))