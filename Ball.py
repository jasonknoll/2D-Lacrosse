import pygame
from random import randint
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0
        self.direction = 0
    def moveUp(self):
        self.y_change = -10
    def moveDown(self):
        self.y_change = 10
    def moveLeft(self):
        self.x_change = -10
    def moveRight(self):
        self.x_change = 10
    def stopVer(self):
        self.y_change = 0
    def stopHor(self):
        self.x_change = 0
    def move(self):
        self.y += self.y_change
        self.x += self.x_change
    def checkEdges(self):
        if self.x <= 0: #if at the left
            if self.direction == 0: #if moving left
                self.direction = 4 #move right
            elif self.direction == 1: #if moving up and left
                self.direction = 3 #move up and right
            elif self.direction == 7: #if moving down and left
                self.direction = 5 #move down and right
        if self.y <= 0: #if at the top
            if self.direction == 2: #if moving up
                self.direction = 6 #move down
            elif self.direction == 3: #if moving up and right
                self.direction = 5 #move down and right
            elif self.direction == 1: #if moving up and left
                self.direction = 7 #move down and left
        if self.x >= 1010: #if at the right
            if self.direction == 3: #if moving up and right
                self.direction = 1 #move up and left
            #continue here
    def faceoff(self):
        self.startDir = randint(0, 7)
        self.direction = self.startDir
    def go(self):
        if self.direction == 0:
            self.moveLeft()
        elif self.direction == 1:
            self.moveLeft()
            self.moveUp()
        elif self.direction == 2:
            self.moveUp()
        elif self.direction == 3:
            self.moveUp()
            self.moveRight()
        elif self.direction == 4:
            self.moveRight()
        elif self.direction == 5:
            self.moveRight()
            self.moveDown()
        elif self.direction == 6:
            self.moveDown()
        elif self.direction == 7:
            self.moveDown()
            self.moveLeft()


