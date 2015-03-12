#!/usr/bin/python

import pygame, sys

from pygame.locals import *
from objects.Ball import *
from objects.Brick import *
from objects.Paddle import *

paddle = None
ball = None


def initialize_pygame():

    pygame.init()

    X = 600
    Y = 480

    display = pygame.display.set_mode((X,Y), 0, 32)

    pygame.display.set_caption('Breakout')
    pygame.mouse.set_visible(False)

    return display

def initialize_game(display):
    sprites = []

    global ball
    ball = Ball(100, 100, display)
    sprites.append(ball)

    global paddle
    paddle = Paddle(85, 12, 0, display)
    sprites.append(paddle)

    return sprites


def CheckCollision(sprites):
    ball.checkCollision(paddle)

def main():

    display = initialize_pygame()
    sprites = initialize_game(display)


    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        display.fill((0,0,0))

        CheckCollision(sprites)

        for sprite in sprites:
            sprite.update()
            sprite.draw()

        pygame.time.Clock().tick(60)


if __name__ == "__main__":
    main()