#################################################
#                   INPUT
# Programação de Jogos 4
# Campo Minado / Movimento
#
# Usage:
# > python3 Input04PJ04_c.py
#
# v2.072
# 20171228
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import os, sys, pygame
import random


# load image function
def load_image(file):
    path = os.path.join('images', file)
    return pygame.image.load(path).convert_alpha()


# screen
class Setupscreen(object):
    """Starts a screen and displays background"""
    def __init__(self, image_file):
        # physical parameters
        self.size = (640, 480)
        self.bgcolour = [90, 230, 90]
        # the canvas
        self.area = pygame.display.set_mode(self.size)
        # background image and its enclosing rectangle
        self.image = load_image(image_file)
        self.rect = self.image.get_rect()
        # show image
        self.show()

    def show(self):
        # fill screen with solid colour
        self.area.fill(self.bgcolour)
        # blit the image
        self.area.blit(self.image, (0, 0))


# tank
class Tank(object):
    """Creates the player's tank and controls how it moves"""
    def __init__(self, x, y):
        self.image = load_image('tank4.png')
        self.pos = self.image.get_rect().move(x, y)

    def move(self):
        # movement rules
        self.pos.left += 2
        

# tankmovement

# paratrooper

# skydmovement


# event loop
def eventloop(scr, tnk):
    while 1:
        # quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        # blit the background to erase the last tank position
        scr.area.blit(scr.image, tnk.pos, tnk.pos)
        # move tank
        tnk.move()
        # blit tank in new position
        scr.area.blit(tnk.image, tnk.pos)
        # refresh display
        pygame.display.flip()


# main routine
def main():
    print('Main')
    # start Pygame
    pygame.init()
    # start the display
    screen = Setupscreen('desert640.png')
    # creates tank
    thetank = Tank(50, 300)
    # start the event loop
    eventloop(screen, thetank)


# execute main
if __name__ == '__main__': 
    main()


