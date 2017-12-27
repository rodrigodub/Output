#################################################
#                   INPUT
# Programação de Jogos 4
# Campo Minado / Movimento
#
# Usage:
# >python3 Input04PJ04_c.py
#
# v2.061
# 20171227
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import sys, pygame
import random


# define screen
def setscreen():
    size = (640, 480)
    backgroundimage = './images/desert640.png'
    background = pygame.image.load(backgroundimage)
    screen = pygame.display.set_mode(size)
    screen.blit(background, size)
    return screen


# event loop
def eventloop():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        pygame.display.flip()


# main routine
def main():
    print('Main')
    pygame.init()
    setscreen()
    eventloop()


# execute main
main()


