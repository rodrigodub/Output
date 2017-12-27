#################################################
#                   INPUT
# Programação de Jogos 4
# Campo Minado / Movimento
#
# Usage:
# >python3 Input04PJ04_c.py
#
# v2.064
# 20171227
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import sys, pygame
import random


# background
class Background(object):
    def __init__(self, image_file):
        # pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = 0,0


# screen
class Setscreen(object):
    def __init__(self, bg):
        self.size = (640,480)
        self.bgcolor = [90, 230, 90]
        self.show(bg)
    
    def show(self, bg):
        screen = pygame.display.set_mode(self.size)
        screen.fill(self.bgcolor)
        screen.blit(Background(bg).image, (0,0))
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
    screen = Setscreen('images/desert640.png')
    eventloop()


# execute main
main()


