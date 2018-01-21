#################################################
#                   INPUT
# Programação Basic 6
# O que são variáveis
#
# Usage:
# > python3 Input05PB06_b.py
#
# v2.099
# 20180121
#################################################
__author__ = 'Rodrigo Nobrega'

# global variables
# prices in R$, Jan 2018
ETH = 3.199
GAS = 4.299
DIE = 3.699


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
        self.coords = [262, 255, 275]
        self.position = 0
        self.price = 0

    def select(self):
        keys = pygame.key.get_pressed()
        if keys[K_e]:
            self.option = self.type[0]
            self.position = self.coords[0]
            self.price = ETH
        if keys[K_g]:
            self.option = self.type[1]
            self.position = self.coords[1]
            self.price = GAS
        if keys[K_d]:
            self.option = self.type[2]
            self.position = self.coords[2]
            self.price = DIE


# tank fill
class Fill(object):
    """Fill the tank"""
    def __init__(self):
        self.volume = 0

    def press(self):
        keys = pygame.key.get_pressed()
        if self.volume <= 70:
            if keys[K_SPACE]:
                self.volume += 0.01


# event loop MAIN
def eventloopmain(scr, fnt1, fnt2, opt, pmp):
    # arguments: scr=screen, fntn=font, opt=fuel option, pmp=pump
    a = 1
    while a == 1:
        # quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                sys.exit()
        # switch between event loops
        if opt.option == '':
            # choose fuel
            eventloop1(scr, fnt1, opt)
        else:
            # fill tank
            eventloop2(scr, fnt1, fnt2, opt, pmp)


# event loop CHOICE
def eventloop1(scr, fnt, opt):
    # arguments: scr=screen, fnt=font, opt=fuel option
    scr.area.blit(scr.image, (0, 0))
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
        scr.area.blit(writetext(fnt, 'Press Q to quit', (100, 100, 100)), (255, 290))
        # check option
        opt.select()
        if opt.option != '':
            a = 0
        # refresh display
        pygame.display.update()


# event loop TANK FILL
def eventloop2(scr, fnt1, fnt2, opt, pmp):
    # arguments: scr=screen, fntn=font, opt=fuel option, pmp=pump
    # clear screen (part of it)
    scr.area.blit(scr.image, (230, 145, 180, 165), (230, 145, 180, 165))
    a = 1
    while a == 1:
        # quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                sys.exit()
        # write text
        scr.area.blit(writetext(fnt1, 'Press SPACE to fill, P to pay and finish', (100, 100, 100)), (160, 150))
        scr.area.blit(writetext(fnt2, '{}'.format(opt.option), (180, 100, 100)), (opt.position, 170))
        scr.area.blit(writetext(fnt1, 'R$ {} / L'.format(opt.price), (100, 100, 100)), (270, 212))
        # volume and price
        scr.area.blit(writetext(fnt1, 'Litres', (100, 100, 100)), (150, 290))
        scr.area.blit(writetext(fnt1, 'R$', (100, 100, 100)), (470, 290))
        # fill tank
        pmp.press()
        # number of litres
        scr.area.blit(scr.image, (100, 310, 140, 40), (100, 310, 140, 40))
        scr.area.blit(writetext(fnt2, '{}'.format(round(pmp.volume, 3)), (0, 0, 0)), (130, 310))
        # value in Real
        scr.area.blit(scr.image, (410, 310, 140, 40), (410, 310, 140, 40))
        scr.area.blit(writetext(fnt2, '{}'.format(round(pmp.volume * opt.price, 2)), (0, 0, 0)), (425, 310))
        # tests payment
        if pygame.key.get_pressed()[K_p]:
            # initialise volume, clear option, exist loop
            pmp.volume = 0
            opt.option = ''
            a = 0
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
    screen = Setupscreen('background green 640x480.png')
    # create choice
    option = Choice()
    # turn on pump
    pump = Fill()
    # starts the event loop MAIN
    eventloopmain(screen, font1, font2, option, pump)


# execute main
if __name__ == '__main__': 
    main()


