__author__ = 'Joshua'

import pygame

class Paddle(object):
    def __init__(self, height, width, X, display):
        self.height = height
        self.width = width
        self.display = display

        self.X = X
        self.Y = 350

    def paddle_update(self, X):
        self.X = X

    def draw_paddle(self):
        pygame.draw.rect(self.display, (255,255,255), (self.X,self.Y,self.height,self.width))