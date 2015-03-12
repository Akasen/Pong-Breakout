#!/usr/bin/python
__author__ = 'Joshua'

import pygame, sys
pygame.init()

from pygame.locals import *

FPS = 60
fpsClock = pygame.time.Clock()

#X AND Y VALUE OF WINDOW
X = 600
Y = 480

DISPLAYSURF = pygame.display.set_mode((X,Y), 0, 32)

pygame.display.set_caption('Breakout')

from objects.Ball import *
from objects.Brick import *
from objects.Paddle import *


#Movement commands
def move_right(ball):

    ball.ballX += ball.ballSpeedX


def move_left(ball):

    ball.ballX -= ball.ballSpeedX


def move_down(ball):

    ball.ballY -= ball.ballSpeedY


def move_up(ball):

    ball.ballY += ball.ballSpeedY


def distance():
    pass

def collision_detection(ball):

    if ball.ballX >= X:
        ball.ballSpeedX = -ball.ballSpeedX

    if ball.ballX < 0:
        ball.ballSpeedX = -ball.ballSpeedX

    if ball.ballY >= Y:
        ball.ballSpeedY = -ball.ballSpeedY

    if ball.ballY < 0:
        ball.ballSpeedY = -ball.ballSpeedY

def collision(ball, paddle):
    if ball.ballX <= paddle.X & ball.ballY <= paddle.Y:
        ball.ballSpeedY = -ball.ballSpeedY

# Movement commands ends

def init_blocks():
    x = 20
    y = 25

    i = 0
    j = 0

    while j < 3:
        while i < 6:
            pygame.draw.rect(DISPLAYSURF, (255,255,255), (x,y, 65,20))
            x += 100

            i += 1
        y += 50
        j += 1

#SOMETHING NEEDS TO UPDATE THE FRAME RATE
#KEEP THE BALL FROM MOVING TOO FAST
def update(ball):
    ball.draw_ball()


def main():

    #init_blocks()

    pygame.mouse.set_visible(False)

    ball = Ball(100, 100, DISPLAYSURF)
    mouseX = 0
    paddle = Paddle(85,12, mouseX, DISPLAYSURF)


    while True:

        #init_blocks()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if pygame.key.get_pressed() [K_RIGHT]:
                    ball.ballX = move_right(ball)

            if event.type == MOUSEMOTION:
                mouseX = pygame.mouse.get_pos()[0]
                #print mouseX
                paddle.paddle_update(mouseX)


        paddle.draw_paddle()
        move_right(ball)
        move_down(ball)

        collision_detection(ball)
        collision(ball, paddle)

        update(ball)


        pygame.display.update()
        DISPLAYSURF.fill((0,0,0))
        fpsClock.tick(FPS)

main()