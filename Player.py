import pygame
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isPlayer = False
        self.isChasingPlayer = False
        self.isBlue = False
        self.y_change = 0
        self.x_change = 0
    def moveUp(self):
        self.y_change = -5
    def moveDown(self):
        self.y_change = 5
    def moveLeft(self):
        self.x_change = -5
    def moveRight(self):
        self.x_change = 5
    def stopVer(self):
        self.y_change = 0
    def stopHor(self):
        self.x_change = 0
    def move(self):
        self.y += self.y_change
        self.x += self.x_change
    def checkEdges(self):
        if self.x >= 1000:
            self.stopHor()
            self.moveLeft()
        if self.x <= 0:
            self.stopHor()
            self.moveRight()
        if self.y >= 550:
            self.stopVer()
            self.moveUp()
        if self.y <= 0:
            self.stopVer()
            self.moveDown()
