__author__ = 'Joshua'

import pygame

class Ball(object):
    def __init__(self, x, y, display):
        self.x = x
        self.y = y
        self.display = display

        self.speed_x = 5
        self.speed_y = 5

        self.color = (255, 255, 255)
        self.radius = 10

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        pygame.draw.circle(self.display, self.color, (self.x, self.y), self.radius)

    def checkCollision(self, paddle):
        if(self.x + self.radius >= paddle.x and self.x <= paddle.x + (paddle.width)):
            if(self.y + self.radius >= paddle.y and self.y + (0.9 * self.radius) <= paddle.y):
                self.speed_y = -5

        if(self.x + (2 * self.radius) > 600):
            self.speed_x = -5
        elif(self.x <= 0):
            self.speed_x = 5
        if(self.y + (2 * self.radius) > 480):
            self.speed_y = -5
        elif(self.y <= 0):
            self.speed_x = 5

