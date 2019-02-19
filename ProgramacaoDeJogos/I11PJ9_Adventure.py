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
# v2.302
# 20190219
#################################################
__author__ = 'Rodrigo Nobrega'


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
    def __init__(self, position):
        self.position = position
        # self.directions = {'north': 0, 'south': 0, 'east': 0, 'west': 0}

    def description(self):
        raise NotImplementedError

    def modifyplayer(self):
        raise NotImplementedError


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
    class Entrance(Location):
        def __init__(self, loc):
            super().__init__(loc)
            # self.directions = {'north': 10, 'south': 22, 'east': 17, 'west': 15}

        def description(self):
            return 'You are in the entrance hall.'

        def modifyplayer(self):
            pass

    entrance = Entrance(16)
    # entrance.description() = 'You are in the entrance hall.'
    return {entrance.position:entrance}


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
    world = setupworld()
    print(world[16].description())


# execute main
if __name__ == '__main__':
    # main()
    test()

