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
# 20190309
#################################################
__author__ = 'Rodrigo Nobrega'
__version__ = 'v2.314'


# import
import os
import sys
import pygame
from pygame.locals import *
import numpy as np
# import random
# import math


# Global variables
SCREENSIZE = (1024, 576)
BLACK = (0, 0, 0)
BACKGROUND = (0, 196, 0)
PIXELCOLOR = (255, 192, 128)
BORDER = (255, 128, 128)
LINESIZE = 60
keyboardentry = ''


# load image function
def load_image(file):
    path = os.path.join('images/', file)
    return pygame.image.load(path).convert_alpha()


# write text
def writetext(font, text, colour):
    # colour: tuple (r, g, b)
    a = font.render(text, 0, colour)
    return a


# create line breaks
def addlinebreaks(txt, size):
    result = ''
    while len(txt) > size:
        head = txt[0:size]
        tail = txt[size:]
        result += head.rsplit(' ', 1)[0] + '\n'
        txt = head.rsplit(' ', 1)[1] + tail
    result += txt
    return result


# convert to multi lines


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
    def __init__(self, position):
        self.position = position
        self.inventory = []


# World setup functions
def map():
    a = np.arange(24)+1
    b = a.reshape(4, 6)
    return b

def setupworld():
    worlddict = {4: Location("Outside", "You are outside a large building. The floor is full of sand.")
                 , 7: Location("River", "You are at the margin of a fast flowing river. It doesn't seem easy to cross.")
                 , 8: Location("Forest", "You are in a petrified forest. It is dark and very humid. You feel cold. "
                                         "The noise of birds and insects is very loud. You have the impression you're "
                                         "getting mad.")
        , 10: Location("Dusty Room", "You are in a dusty room. There are lots of spider webs and the furniture is "
                                     "covered by a thick layer of dust.")
                 , 11: Location("Dark Room", "You are in a dark room. There is absolutely no light. It's too dark "
                                             "and you can't see anything.")
                 , 14: Location("Path", "You are on a muddy path. Your boots are sticking in the mud and it's hard "
                                        "to walk.")
                 , 15: Location("Gate", "You are by the gate to the hidden city. What mysteries lay behind it?")
        , 16: Location("Entrance Hall", "You are in the entrance hall. It's a white room with walls covered with an"
                                        " aged wallpaper with a pattern of green leaves.")
                 , 17: Location("Courtyard", "You are in the courtyard.")
                 , 18: Location("Garden", "You are in the garden.")
                 , 22: Location("Cupboard", "You are in the cupboard.")
                 , 24: Location("Throne", "You are in the Throne room. The view is spectacular and wealth "
                                          "shines everywhere.")}
    return worlddict


# captures keyboard events
def keyboardcapture(entry):
    string = entry
    keys = pygame.key.get_pressed()
    if keys[K_RETURN]:
        string = ''
    elif keys[K_BACKSPACE]:
        string = string[:-1]
    elif keys[K_a]:
        string += 'a'
    return string


# screen
class Screen(object):
    """Starts a screen and displays background"""
    def __init__(self, image_file=None):
        # physical parameters
        self.size = SCREENSIZE
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
def eventloop(scr, fnt, clk, map, wld, ply, kbentry):
    # arguments: scr=screen, fnt=font, clk=clock, map=themap, wld=world, ply=player
    a = 1
    while a == 1:
        # quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                sys.exit()
        # measure time
        clk.tick(60)
        # iterate the game state
        txt = enumerate(addlinebreaks(wld[ply.position].description, LINESIZE).split('\n'))
        # keyboard entry
        kbentry = keyboardcapture(kbentry)
        # clears screen and write text
        # scr.display.blit(scr.image, (120, 5, 50, 30), (120, 5, 50, 30))
        pygame.draw.rect(scr.display, BACKGROUND, (0, 0, 1024, 576), 0)
        for i in txt:
            scr.display.blit(writetext(fnt, '{}'.format(i[1]), BLACK), (50, (30 * i[0])+50))
        scr.display.blit(writetext(fnt, '> abc{}'.format(kbentry), BLACK), (50, 500))
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
    # creates the map
    themap = map()
    world = setupworld()
    player = Player(16)
    # start the event loop
    eventloop(screen, font1, clock, themap, world, player, keyboardentry)


# test routine
def test():
    themap = map()
    world = setupworld()
    #
    print('\nThe Map:\n', themap, '\n')
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
    print('My position exist in the map? ', myposition in themap)
    mylocationinmap = np.where(themap == myposition)
    print('Where is my position located on the map? ', mylocationinmap)
    southofme = ([mylocationinmap[0] + 1, mylocationinmap[1]])
    # southofme = themap[mylocationinmap[0] + 1, mylocationinmap[1]]
    print('What is in the South? ', southofme)
    print('What value is in the South? ', themap[tuple(southofme)])
    print('Is the South available? ', themap[tuple(southofme)][0] in available)
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
    main()
    # test()

