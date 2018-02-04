#################################################
#                   UDG
# A script to help program
# User Defined Graphics
#
# Usage:
# > python3 UDG.py
#
# v2.130
# 20180204
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import os, sys, pygame
from pygame.locals import *
import numpy as np
# import random
# import math


# load image function
def load_image(file):
    path = os.path.join('images', file)
    return pygame.image.load(path).convert_alpha()


# write text
def writetext(font, text, colour):
    # colour: tuple (r, g, b)
    a = font.render(text, 0, colour)
    return a


# screen
class Screen(object):
    """Starts a screen and displays background"""
    def __init__(self, image_file=None):
        # physical parameters
        self.size = (1024, 576)
        self.bgcolour = [230, 230, 230]
        # the canvas
        self.display = pygame.display.set_mode(self.size)
        self.title = pygame.display.set_caption('User Defined Graphics app')
        # background image and its enclosing rectangle
        if image_file:
            self.image = load_image(image_file)
            self.rect = self.image.get_rect()
        else:
            self.image = ''
            self.rect = Rect(0, 0, 0, 0)
        # show image
        self.show()

    def show(self):
        # fill screen with solid colour
        self.display.fill(self.bgcolour)
        # blit background image
        if self.image != '':
            self.display.blit(self.image, (0, 0))


# the big grid
class Grid(object):
    """This is the large scale grid"""
    def __init__(self):
        self.array = np.zeros((8, 8))
        #self.array[7, 7] = 1

    def drawpixels(self, scr):
        for i in range(0, 8):
            for j in range(0, 8):
                pygame.draw.rect(scr.display, self.pixelcolor(j, i), ((i*50)+100, (j*50)+100, 50, 50), 0)

    def drawgrid(self, scr):
        for i in range(100, 550, 50):
            pygame.draw.line(scr.display, (0, 0, 0), (i, 100), (i, 500))
            pygame.draw.line(scr.display, (0, 0, 0), (100, i), (500, i))

    def pixelcolor(self, i, j):
        if self.array[i, j] == 0:
            return (230, 255, 230)
        else:
            return (0, 0, 0)


# the cursor
class Cursor(object):
    def __init__(self):
        self.pos = [0, 0]
        self.posprev = [0, 0]
        self.size = [(50, 50), (75, 50)]

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.posprev[1] = self.pos[1]
            self.pos[1] -= 1
            if self.pos[1] < 0:
                self.pos[1] = 7
        if keys[K_DOWN]:
            self.posprev[1] = self.pos[1]
            self.pos[1] += 1
            if self.pos[1] > 7:
                self.pos[1] = 0
        if keys[K_LEFT]:
            self.posprev[0] = self.pos[0]
            self.pos[0] -= 1
            if self.pos[0] < 0:
                self.pos[0] = 8
        if keys[K_RIGHT]:
            self.posprev[0] = self.pos[0]
            self.pos[0] += 1
            if self.pos[0] > 8:
                self.pos[0] = 0

    def draw(self, scr):
        if self.pos[0] < 8:
            pygame.draw.rect(scr.display, (230, 255, 230)
                             , ((self.posprev[0] * 50 + 100), (self.posprev[1] * 50 + 100)
                                , (self.size[0][0]), (self.size[0][1]))
                             , 0)
            pygame.draw.rect(scr.display, (255, 255, 200)
                             , ((self.pos[0]*50 + 100), (self.pos[1]*50 + 100)
                                , (self.size[0][0]), (self.size[0][1]))
                             , 0)
        else:
            pygame.draw.rect(scr.display, (255, 255, 200)
                             , ((self.pos[0] * 50 + 200), (self.pos[1] * 50 + 100)
                                , (self.size[1][0]), (self.size[1][1]))
                             , 0)


# event loop
def eventloop(scr, fnt, clk, grd, csr):
    # arguments: scr=screen, fnt=font, clk=clock, grd=big grid, csr=cursor
    a = 1
    while a == 1:
        # quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                sys.exit()
        # measure time
        clk.tick(10)
        # write text
        # scr.display.blit(scr.image, (120, 5, 50, 30), (120, 5, 50, 30))
        scr.display.blit(writetext(fnt, 'UDG', (100, 100, 100)), (10, 10))
        # draw pixels
        grd.drawpixels(scr)
        # draw cursor
        csr.move()
        csr.draw(scr)
        # draw grid
        grd.drawgrid(scr)
        # refresh display
        pygame.display.update()


# main routine
def main():
    print('\n ::: UDG app :::\n\n       Press [Q] to quit.\n')
    # start Pygame
    pygame.init()
    pygame.mixer.init()
    font1 = pygame.font.Font('./fonts/Chicago Normal.ttf', 16)
    clock = pygame.time.Clock()
    score = 0
    # start the display
    screen = Screen()
    # start the big grid
    grid = Grid()
    # create cursor
    cursor = Cursor()
    # start the event loop with tank moving right
    eventloop(screen, font1, clock, grid, cursor)


# execute main
if __name__ == '__main__': 
    main()


