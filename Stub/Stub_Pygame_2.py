#################################################
#                   UDG
# A script to help program
# User Defined Graphics
#
# BR: Input 25 Aplicacoes 13
# 
# Usage:
# > python3 UDG.py
#
# v.3.022
# 20180204 / 20230707
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import os, sys, pygame
from pygame.locals import *
import numpy as np
# import random
# import math


# Global variables
BLACK = (0, 0, 0)
BACKGROUND = (230, 230, 230)
PIXELCOLOR = (255, 255, 255)
HIGHLIGHT = (255, 128, 128)


# load image function
def load_image(file):
    path = os.path.join('images', file)
    return pygame.image.load(path).convert_alpha()


# write text
def writetext(font, text, colour):
    # colour: tuple (r, g, b)
    a = font.render(text, 0, colour)
    return a


# eight-bit string
def eightbitstring(num):
    return '00000000{}'.format(bin(num)[2:])[-8:]


# screen
class Screen(object):
    """Starts a screen and displays background"""
    def __init__(self, image_file=None):
        # physical parameters
        self.size = (1024, 576)
        self.bgcolour = BACKGROUND
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
            pygame.draw.line(scr.display, BLACK, (i, 100), (i, 500))
            pygame.draw.line(scr.display, BLACK, (100, i), (500, i))

    def pixelcolor(self, i, j):
        if self.array[i, j] == 0:
            return PIXELCOLOR
        else:
            return BLACK


# the cursor
class Cursor(object):
    def __init__(self):
        self.pos = [0, 0]
        self.posprev = [0, 0]
        self.size = [(50, 50), (75, 50)]

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.posprev = [i for i in self.pos]
            self.pos[1] -= 1
            if self.pos[1] < 0:
                self.pos[1] = 7
        if keys[K_DOWN]:
            self.posprev = [i for i in self.pos]
            self.pos[1] += 1
            if self.pos[1] > 7:
                self.pos[1] = 0
        if keys[K_LEFT]:
            self.posprev = [i for i in self.pos]
            self.pos[0] -= 1
            if self.pos[0] < 0:
                self.pos[0] = 8
        if keys[K_RIGHT]:
            self.posprev = [i for i in self.pos]
            self.pos[0] += 1
            if self.pos[0] > 8:
                self.pos[0] = 0

    def draw(self, scr):
        if self.pos[0] < 8:
            # clears previous on the grid and on the codes
            pygame.draw.rect(scr.display, PIXELCOLOR
                             , ((self.posprev[0] * 50 + 100), (self.posprev[1] * 50 + 100)
                                , (self.size[0][0]), (self.size[0][1]))
                             , 0)
            pygame.draw.rect(scr.display, BACKGROUND
                             , ((600), (self.pos[1] * 50 + 100)
                                , (self.size[1][0]), (self.size[1][1]))
                             , 0)
            pygame.draw.rect(scr.display, BACKGROUND
                             , ((500), (self.pos[1] * 50 + 100)
                                , (self.size[0][0]), (self.size[0][1]))
                             , 0)
            # draws current
            pygame.draw.rect(scr.display, HIGHLIGHT
                             , ((self.pos[0]*50 + 100), (self.pos[1]*50 + 100)
                                , (self.size[0][0]), (self.size[0][1]))
                             , 0)
        else:
            # clears previous
            pygame.draw.rect(scr.display, BACKGROUND
                             , ((600), (self.posprev[1] * 50 + 100)
                                , (self.size[1][0]), (self.size[1][1]))
                             , 0)
            pygame.draw.rect(scr.display, BACKGROUND
                             , ((500), (self.pos[1] * 50 + 100)
                                , (self.size[0][0]), (self.size[0][1]))
                             , 0)
            # draws current
            pygame.draw.rect(scr.display, HIGHLIGHT
                             , ((self.pos[0] * 50 + 200), (self.pos[1] * 50 + 100)
                                , (self.size[1][0]), (self.size[1][1]))
                             , 0)


# the Data array
class Udg(object):
    def __init__(self):
        self.array = [0, 0, 0, 0, 0, 0, 0, 0]
        # mode: M=decimal, H=hex
        self.mode = 'M'

    def clearlist(self, scr):
        for i in range(0, 8):
            pygame.draw.rect(scr.display, BACKGROUND, (600, (i*50)+100, 75, 50), 0)

    def list(self, scr: Screen, fnt):
        for i in range(0, 8):
            scr.display.blit(writetext(fnt, '{}'.format(self.array[i]), BLACK), (630, (i*50)+115))

    def changenumber(self, csr: Cursor):
        if csr.pos[0] == 8:
            keys = pygame.key.get_pressed()
            if keys[K_1] and int('{}1'.format(self.array[csr.pos[1]])[-3:]) <= 255:
                self.array[csr.pos[1]] = int('{}1'.format(self.array[csr.pos[1]])[-3:])
            elif keys[K_1]:
                self.array[csr.pos[1]] = 1
            if keys[K_2] and int('{}2'.format(self.array[csr.pos[1]])[-3:]) <= 255:
                self.array[csr.pos[1]] = int('{}2'.format(self.array[csr.pos[1]])[-3:])
            elif keys[K_2]:
                self.array[csr.pos[1]] = 2
            if keys[K_3] and int('{}3'.format(self.array[csr.pos[1]])[-3:]) <= 255:
                self.array[csr.pos[1]] = int('{}3'.format(self.array[csr.pos[1]])[-3:])
            elif keys[K_3]:
                self.array[csr.pos[1]] = 3
            if keys[K_4] and int('{}4'.format(self.array[csr.pos[1]])[-3:]) <= 255:
                self.array[csr.pos[1]] = int('{}4'.format(self.array[csr.pos[1]])[-3:])
            elif keys[K_4]:
                self.array[csr.pos[1]] = 4
            if keys[K_5] and int('{}5'.format(self.array[csr.pos[1]])[-3:]) <= 255:
                self.array[csr.pos[1]] = int('{}5'.format(self.array[csr.pos[1]])[-3:])
            elif keys[K_5]:
                self.array[csr.pos[1]] = 5
            if keys[K_6] and int('{}6'.format(self.array[csr.pos[1]])[-3:]) <= 255:
                self.array[csr.pos[1]] = int('{}6'.format(self.array[csr.pos[1]])[-3:])
            elif keys[K_6]:
                self.array[csr.pos[1]] = 6
            if keys[K_7] and int('{}7'.format(self.array[csr.pos[1]])[-3:]) <= 255:
                self.array[csr.pos[1]] = int('{}7'.format(self.array[csr.pos[1]])[-3:])
            elif keys[K_7]:
                self.array[csr.pos[1]] = 7
            if keys[K_8] and int('{}8'.format(self.array[csr.pos[1]])[-3:]) <= 255:
                self.array[csr.pos[1]] = int('{}8'.format(self.array[csr.pos[1]])[-3:])
            elif keys[K_8]:
                self.array[csr.pos[1]] = 8
            if keys[K_9] and int('{}9'.format(self.array[csr.pos[1]])[-3:]) <= 255:
                self.array[csr.pos[1]] = int('{}9'.format(self.array[csr.pos[1]])[-3:])
            elif keys[K_9]:
                self.array[csr.pos[1]] = 9
            if keys[K_0] and int('{}0'.format(self.array[csr.pos[1]])[-3:]) <= 255:
                self.array[csr.pos[1]] = int('{}0'.format(self.array[csr.pos[1]])[-3:])
            elif keys[K_0]:
                self.array[csr.pos[1]] = 0

    def update(self, grd):
        for i in range(0, 8):
            grd.array[i] = [n for n in eightbitstring(self.array[i])]


# event loop
def eventloop(scr, fnt, clk, grd, csr, udg):
    # arguments: scr=screen, fnt=font, clk=clock, grd=big grid, csr=cursor, udg=udg
    a = 1
    while a == 1:
        # quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                sys.exit()
        # measure time
        clk.tick(10)
        # write text
        #pygame.draw.rect(scr.display, BACKGROUND, (0, 0, 500, 40), 0)
        scr.display.blit(writetext(fnt, 'User Defined Graphics', (100, 100, 100)), (10, 10))
        # draw pixels
        grd.drawpixels(scr)
        # clears the udg data list, for updating
        udg.clearlist(scr)
        # draw cursor
        csr.move()
        csr.draw(scr)
        # draw grid
        grd.drawgrid(scr)
        # writes the udg data list
        udg.list(scr, fnt)
        # changes number
        udg.changenumber(csr)
        # updates grid
        udg.update(grd)
        # refresh display
        pygame.display.update()


# main routine
def main():
    print('\n ::: UDG app :::\n\n       Press [Q] to quit.\n')
    # start Pygame
    pygame.init()
    pygame.mixer.init()
    font1 = pygame.font.Font('./fonts/Chicago Normal.ttf', 18)
    clock = pygame.time.Clock()
    score = 0
    # start the display
    screen = Screen()
    # start the big grid
    grid = Grid()
    # create cursor
    cursor = Cursor()
    # create the UDG list
    udg = Udg()
    # start the event loop with tank moving right
    eventloop(screen, font1, clock, grid, cursor, udg)


# execute main
if __name__ == '__main__': 
    main()


