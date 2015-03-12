__author__ = 'Joshua'

import pygame

class Ball(object):
    def __init__(self, ballX, ballY, display):
        self.ballX = ballX
        self.ballY = ballY
        self.display = display

        self.ballSpeedX = 5
        self.ballSpeedY = 5

        self.DirectionX = 1
        self.DirectionY = 1

        self.COLOR = (255, 255, 255)
        self.SIZE = 10
        self.WIDTH = 10

    def draw_ball(self):
        pygame.draw.circle(self.display, self.COLOR, (self.ballX, self.ballY), 10)

    def collision(self):
        pass
