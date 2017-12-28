#################################################
#                   INPUT
# Programação de Jogos 4
# Campo Minado / Movimento
#
# Usage:
# >python3 Input04PJ04_c.py
#
# v2.067
# 20171228
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import os, sys, pygame
import random


# load image
def load_image(file):
    path = os.path.join('images', file)
    return pygame.image.load(path).convert_alpha()


# background
class Background(object):
    def __init__(self, image_file):
        # pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = load_image(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = 0,0


# screen
class Setscreen(object):
    def __init__(self, bg):
        self.size = (640,480)
        self.bgcolor = [90, 230, 90]
        self.area = pygame.display.set_mode(self.size)
        self.show(bg)
            
    def show(self, bg):
        # screen = pygame.display.set_mode(self.size)
        self.area.fill(self.bgcolor)
        self.area.blit(Background(bg).image, (0,0))
        # return screen

# tank
class Tank(object):
    def __init__(self):
        self.image = load_image('tank4.png')
        self.pos = (50,280)
        

# tankmovement

# skydiver

# skydmovement


# event loop
def eventloop():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        pygame.display.flip()


# main routine
def main():
    print('Main')
    pygame.init()
    screen = Setscreen('desert640.png')
    thetank = Tank()
    screen.area.blit(thetank.image, thetank.pos)
    eventloop()


# execute main
if __name__ == '__main__': 
    main()


