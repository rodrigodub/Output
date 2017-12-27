#################################################
#                   INPUT
# Programação de Jogos 4
# Campo Minado / Movimento
#
# Usage:
# >python3 Input04PJ04_c.py
#
# v2.062
# 20171227
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import sys, pygame
import random


# background
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


# define screen
def setscreen():
    size = (640, 480)
    backgroundimage = 'images/desert640.png'
    background = pygame.image.load(backgroundimage)
    screen = pygame.display.set_mode(size)
    # screen.fill([120,30,0])
    screen.blit(background, (0,0))
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
    screen = setscreen()
    # bg = Background()
    eventloop()


# execute main
main()


