#################################################
#                   INPUT 8
# Programacao de Jogos 7
# Labirinth 2 - Treasure Hunt
# UK : Input 7
# Usage:
# > python3 Input08PJ07.py
#
# v2.145
# 20180211
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import os, sys, pygame
from pygame.locals import *
import numpy as np
import random
# import math


# Global variables
BLACK = (0, 0, 0)
BACKGROUND = (230, 230, 230)
PIXELCOLOR = (255, 255, 255)
BORDER = (255, 128, 128)


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
        self.bgcolour = BACKGROUND
        # the canvas
        self.display = pygame.display.set_mode(self.size)
        self.title = pygame.display.set_caption('Treasure Hunt')
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


# The Maze
class Maze(object):
    def __init__(self):
        # block size
        self.bs = 20
        # number of columns in x and y
        self.nx = int(1024/self.bs)
        self.ny = int(576/self.bs)
        # dim p - p is the labirinth
        self.p = np.zeros((self.nx, self.ny), dtype=int)
        # draw border
        self.border()
        # coordinates
        self.x = 1
        self.y = 1
        # last coordinates
        self.lx = 1
        self.ly = 1
        # maze positions
        self.j = 0
        self.g = 0
        # create maze
        try:
            self.createmaze1()
        except RecursionError:
            print('Recursion Error')

    def border(self):
        # horizontal borders
        for j in range(0, self.nx):
            self.p[j, self.ny-1] = 6
            self.p[j, 0] = 6
        # vertical borders
        for j in range(0, self.ny):
            self.p[0, j] = 6
            self.p[self.nx-1, j] = 6

    def createmaze1(self):
        # direction
        self.j = random.randint(0, 3)
        self.g = self.j
        self.createmaze2()

    def createmaze2(self):
        # increment
        self.y = self.ly + 2 * ((self.j == 0) - (self.j == 2))
        self.x = self.lx + 2 * ((self.j == 3) - (self.j == 1))
        # prevent coord indexes to be greater than array size
        if self.x >= self.nx-1:
            self.x -= self.nx
        if self.y >= self.ny-1:
            self.y -= self.ny
        # but still need to catch exception
        try:
            self.p[self.x, self.y]
        except IndexError:
            self.createmaze3()
        # main routine, change the following two blocks
        if self.p[self.x, self.y] == 0:
            self.p[self.x, self.y] = self.j+1
            self.p[int((self.x + self.lx) / 2), int((self.y + self.ly) / 2)] = 5
            self.lx = self.x
            self.ly = self.y
            self.createmaze1()
        else:
            self.createmaze3()

    def createmaze3(self):
        # choose new direction
        self.j = (self.j + 1) % 4
        if self.j != self.g:
            self.createmaze2()
        else:
            self.createmaze4()

    def createmaze4(self):
        # have to catch de index exception for the last postions
        try:
            self.j = self.p[self.lx, self.ly] - 1
            self.p[self.lx, self.ly] = 5
        except IndexError:
            print('Index Error')
        if self.j < 4:
            self.lx = self.lx - 2 * ((self.j == 3) - (self.j == 1))
            self.ly = self.ly - 2 * ((self.j == 0) - (self.j == 2))
            self.createmaze1()
        else:
            self.createmaze5()

    def createmaze5(self):
        for cnt in range(0, 21):
            self.p[2 + 2 * random.randint(0, int((self.nx - 3)/2)), 1 + random.randint(0, (self.ny - 3))] = 5
            self.p[1 + random.randint(0, (self.nx - 3)), 2 + 2 * random.randint(0, int((self.ny - 3)/2))] = 5

    def drawmargin(self, scr):
        for i in range(0, self.nx):
            pygame.draw.rect(scr.display, BORDER, (i * self.bs, 50, self.bs, self.bs), 0)
            pygame.draw.rect(scr.display, BORDER, (i * self.bs, 556, self.bs, self.bs), 0)
        for j in range(0, self.ny):
            pygame.draw.rect(scr.display, BORDER, (0, j * self.bs + 50, self.bs, self.bs), 0)
            pygame.draw.rect(scr.display, BORDER, (1000, j * self.bs + 50, self.bs, self.bs), 0)
        #
        for i in range(1, self.nx-1):
            for j in range(1, self.ny-1):
                if self.p[i, j] == 0:
                    pygame.draw.rect(scr.display, BLACK, (i * self.bs, (j * self.bs) + 50, self.bs, self.bs), 0)

# Labirinth
# class Labirinth(object):
#     def __init__(self):
#         self.blocksize = 20
#         #self.numbercolumns = 2 * int(0.5 * 1024 / self.blocksize)
#         self.numbercolumns = int(1024 / self.blocksize)
#         #self.numberlines = 2 * int(0.5 * 526 / self.blocksize)
#         self.numberlines = int(526 / self.blocksize)
#         #
#         self.array = np.zeros((49, 25), dtype=np.int16)
#
#     def drawmargin(self, scr):
#         for i in range(0, self.numbercolumns):
#             pygame.draw.rect(scr.display, BORDER, (i * self.blocksize, 50, self.blocksize, self.blocksize), 0)
#             pygame.draw.rect(scr.display, BORDER, (i * self.blocksize, 556, self.blocksize, self.blocksize), 0)
#         for j in range(0, self.numberlines):
#             pygame.draw.rect(scr.display, BORDER, (0, j * self.blocksize + 50, self.blocksize, self.blocksize), 0)
#             pygame.draw.rect(scr.display, BORDER, (1000, j * self.blocksize + 50, self.blocksize, self.blocksize), 0)


# event loop
def eventloop(scr, fnt, clk, maz):
    # arguments: scr=screen, fnt=font, clk=clock, maz=labirinth
    a = 1
    while a == 1:
        # quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                sys.exit()
        # measure time
        clk.tick(60)
        # write text
        # scr.display.blit(scr.image, (120, 5, 50, 30), (120, 5, 50, 30))
        scr.display.blit(writetext(fnt, 'OK', BLACK), (10, 10))
        # draws maze
        maz.drawmargin(scr)
        # refresh display
        pygame.display.flip()


# main routine
def main():
    print('\n ::: Labirinth :::\n\n       Press [Q] to quit.\n')
    # start Pygame
    pygame.init()
    pygame.mixer.init()
    font1 = pygame.font.Font('./fonts/Chicago Normal.ttf', 16)
    clock = pygame.time.Clock()
    # score = 0
    # start the display
    screen = Screen()
    # creates the Labirinth
    maze = Maze()
    # start the event loop
    eventloop(screen, font1, clock, maze)


# execute main
if __name__ == '__main__': 
    main()


