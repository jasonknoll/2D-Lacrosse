#school project
#2.5D sports game (lax)
#Version 0.2

import pygame
import Goal
import Ball
import Player
import Team

#from pygame.locals import *

pygame.init()
disp_width = 1024
disp_height = 600
display = pygame.display.set_mode((disp_width, disp_height))
pygame.display.set_caption("2D Lacrosse")
clock = pygame.time.Clock()

fieldImg = pygame.image.load("field.jpg")
blueA1 = pygame.image.load("blueAttack.jpg")
blueD1 = pygame.image.load("blueD.jpg")
blueM1 = pygame.image.load("blueMiddie.jpg")
ballImg = pygame.image.load("ball.jpg")

black = (0, 0, 0)
white = (255, 255, 255)



g1 = Goal.Goal()
g2 = Goal.Goal()
ball = Ball.Ball(500, 300)
ba1 = Player.Player(786, 150)
ba2 = Player.Player(786, 450)
bd1 = Player.Player(256, 150)
bd2 = Player.Player(256, 450)
ra1 = Player.Player(0, 0)
ra2 = Player.Player(0, 0)
rd1 = Player.Player(0, 0)
rd2 = Player.Player(0, 0)
current = Player.Player(0, 0)
t1 = Team.Team()

def mainMenu():
    pass

def match():
    pass

def pCheckEdges():
    ba1.checkEdges()
    ba2.checkEdges()
    ra1.checkEdges()

def run():
    ba1.isPlayer = True
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if ba1.isPlayer == True: #assign the current player (whoever has the ball)
                ba2.isPlayer = False
                current = ba1
            elif ba2.isPlayer == True:
                ba1.isPlayer = False
                current = ba2
            elif bd1.isPlayer == True:
                ba1.isPlayer = False
                ba2.isPlayer = False
                bd2.isPlayer = False
                current = bd1
            elif bd2.isPlayer == True:
                ba1.isPlayer = False
                ba2.isPlayer = False
                bd1.isPlayer = False
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN: #Move Player with the ball
                if event.key == pygame.K_w:
                    current.moveUp()
                if event.key == pygame.K_d:
                    current.moveRight()
                if event.key == pygame.K_a:
                    current.moveLeft()
                if event.key == pygame.K_s:
                    current.moveDown()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    current.stopVer()
                if event.key == pygame.K_d:
                    current.stopHor()
                if event.key == pygame.K_a:
                    current.stopHor()
                if event.key == pygame.K_s:
                    current.stopVer()
            print(event)
        current.move()
        pCheckEdges()
        pygame.display.update()
        clock.tick(60)
        display.blit(fieldImg, (0, 0))
        display.blit(blueA1, (ba1.x, ba1.y))
        display.blit(blueA1, (ba2.x, ba2.y))
        display.blit(blueD1, (bd1.x, bd1.y))
        display.blit(blueD1, (bd2.x, bd2.y))
        display.blit(ballImg, (ball.x, ball.y))
    pygame.quit()
    quit()

run()