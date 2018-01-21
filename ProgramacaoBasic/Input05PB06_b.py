#################################################
#                   INPUT
# Programação Basic 6
# O que são variáveis
#
# Usage:
# > python3 Input05PB06_b.py
#
# v2.098
# 20180121
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import os, sys, pygame
from pygame.locals import *
# import random
# import time


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
class Setupscreen(object):
    """Starts a screen and displays background"""
    def __init__(self, image_file=None):
        # physical parameters
        self.size = (640, 480)
        self.bgcolour = [230, 230, 230]
        # the canvas
        self.area = pygame.display.set_mode(self.size)
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
        self.area.fill(self.bgcolour)
        # blit background image
        if self.image != '':
            self.area.blit(self.image, (0, 0))


# fuel choice
class Choice(object):
    """Chooses between the available fuel"""
    def __init__(self):
        self.option = ''
        self.type = ['Ethanol', 'Gasoline', 'Diesel']

    def select(self):
        keys = pygame.key.get_pressed()
        if keys[K_e]:
            self.option = self.type[0]
        if keys[K_g]:
            self.option = self.type[1]
        if keys[K_d]:
            self.option = self.type[2]



# tank fill


# event loop CHOICE
def eventloop1(scr, fnt, opt):
    # arguments: scr=screen, fnt=font, opt=fuel option
    a = 1
    while a == 1:
        # quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                sys.exit()
        # write text
        scr.area.blit(writetext(fnt, 'Input 05', (0, 0, 0)), (285, 10))
        scr.area.blit(writetext(fnt, 'Programacao Basic 6', (0, 0, 0)), (235, 26))
        scr.area.blit(writetext(fnt, 'Choose the Fuel Type', (100, 100, 100)), (235, 150))
        scr.area.blit(writetext(fnt, opt.type[0], (0, 0, 0)), (285, 200))
        scr.area.blit(writetext(fnt, opt.type[0][0], (180, 100, 100)), (285, 200))
        scr.area.blit(writetext(fnt, opt.type[1], (0, 0, 0)), (285, 220))
        scr.area.blit(writetext(fnt, opt.type[1][0], (180, 100, 100)), (285, 220))
        scr.area.blit(writetext(fnt, opt.type[2], (0, 0, 0)), (285, 240))
        scr.area.blit(writetext(fnt, opt.type[2][0], (180, 100, 100)), (285, 240))
        # check option
        opt.select()
        if opt.option != '':
            a = 0
        # refresh display
        pygame.display.update()


# event loop TANK FILL
def eventloop2(scr, fnt1, fnt2, opt):
    # arguments: scr=screen, fntn=font, opt=fuel option
    # clear screen (part of it)
    scr.area.blit(scr.image, (230, 145, 180, 115), (230, 145, 180, 115))
    a = 1
    while a == 1:
        # quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                sys.exit()
        # write text
        scr.area.blit(writetext(fnt1, 'Press N to fill', (100, 100, 100)), (260, 150))
        scr.area.blit(writetext(fnt2, '{}'.format(opt.option), (180, 100, 100)), (260, 170))
        # refresh display
        pygame.display.update()


# main routine
def main():
    print('\n ::: Input 05 - Variables :::\n\n       Press [Q] to quit.\n')
    # start Pygame
    pygame.init()
    pygame.mixer.init()
    font1 = pygame.font.Font('./fonts/Chicago Normal.ttf', 16)
    font2 = pygame.font.Font('./fonts/Chicago Normal.ttf', 32)
    # start the display
    # screen = Setupscreen()
    screen = Setupscreen('background green 640x480.png')
    #create choice
    option = Choice()
    # starts the event loop CHOICE
    eventloop1(screen, font1, option)
    # starts the event loop TANK FILL
    eventloop2(screen, font1, font2, option)


# execute main
if __name__ == '__main__': 
    main()


