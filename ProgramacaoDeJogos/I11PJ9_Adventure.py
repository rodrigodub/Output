#################################################
#                   INPUT 11
# Programacao de Jogos 9
# The Adventure
#
# UK : Input 9-13
# Wireframe #6
# How to write a Text Adventure:
# https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python/
#
# Usage:
# > python3 I11PJ9_Adventure.py
#
# 20190221
#################################################
__author__ = 'Rodrigo Nobrega'
__version__ = 'v2.304'


# import
import os
import sys
import pygame
from pygame.locals import *
import numpy as np
# import random
# import math


# Global variables
BLACK = (0, 0, 0)
BACKGROUND = (230, 230, 230)
PIXELCOLOR = (255, 192, 128)
BORDER = (255, 128, 128)


# load image function
def load_image(file):
    path = os.path.join('images/', file)
    return pygame.image.load(path).convert_alpha()


# write text
def writetext(font, text, colour):
    # colour: tuple (r, g, b)
    a = font.render(text, 0, colour)
    return a


# Adventure base classes
class Location(object):
    """"Base class for the Map tiles"""
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Item(object):
    """"Base class for the Items"""
    def __init__(self):
        pass


class Enemy(object):
    """"Base class for the Enemy"""
    def __init__(self):
        pass


class Player(object):
    """"Base class for the Player"""
    def __init__(self):
        pass


# World setup functions
def map():
    a = np.arange(24)+1
    b = a.reshape(4, 6)
    return b


def setupworld():
    worlddict = {10: Location("Dusty Room", "You are in a dusty room. There are lots of spider webs and the "\
                                           "furniture is covered by a thick layer of dust.")
        , 16: Location("Entrance Hall", "You are in the entrance hall. It's a white room with green leaves wallpaper.")}
    return worlddict


# screen
class Screen(object):
    """Starts a screen and displays background"""
    def __init__(self, image_file=None):
        # physical parameters
        self.size = (1024, 576)
        self.bgcolour = BACKGROUND
        # the canvas
        self.display = pygame.display.set_mode(self.size)
        self.title = pygame.display.set_caption('--ADVENTURE--')
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


# event loop
def eventloop(scr, fnt, clk):
    # arguments: scr=screen, fnt=font, clk=clock
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
        # refresh display
        pygame.display.flip()


# main routine
def main():
    print('\n ::: Adventure :::\n\n       Press [Q] to quit.\n')
    # start Pygame
    pygame.init()
    pygame.mixer.init()
    font1 = pygame.font.Font('./fonts/Chicago Normal.ttf', 16)
    clock = pygame.time.Clock()
    # score = 0
    # start the display
    screen = Screen()
    # start the event loop
    eventloop(screen, font1, clock)


# test routine
def test():
    mapa = map()
    world = setupworld()
    #
    print('\nThe Map:\n', mapa, '\n')
    #
    print('\nThe World:\n', world, '\n')
    #
    for k, v in world.items():
        print('{}: {} / {}'.format(k, v.name, v.description))
    #
    myposition = 16
    available = world.keys()
    print('\nMy position: ', myposition)
    print('Available positions: ', available)
    print('My position exist in the available positions? ', myposition in available)
    print('My position exist in the map? ', myposition in mapa)
    mylocationinmap = np.where(mapa == myposition)
    print('Where is my position located on the map? ', mylocationinmap)
    southofme = ([mylocationinmap[0] + 1, mylocationinmap[1]])
    # southofme = mapa[mylocationinmap[0] + 1, mylocationinmap[1]]
    print('What is in the South? ', southofme)
    print('What value is in the South? ', mapa[southofme])
    print('Is the South available? ', mapa[southofme][0] in available)
    # print(mylocationinmap[0])
    # print(mylocationinmap[0] + 1)
    # print(mapa[2, 3])
    # print(mapa[mylocationinmap[0], mylocationinmap[1]])
    # print(mapa[mylocationinmap[0], mylocationinmap[1]] + 1)
    # print(mapa[mylocationinmap[0], mylocationinmap[1] + 1])
    # print(mapa[mylocationinmap[0] + 1, mylocationinmap[1]])
    # print(mapa[mylocationinmap[0] + 1, mylocationinmap[1]][0])
    # print(mapa[mylocationinmap[0] + 1, mylocationinmap[1]][0] in available)


# execute main
if __name__ == '__main__':
    # main()
    test()

