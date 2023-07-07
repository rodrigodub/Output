#################################################
#                   INPUT
# Programação de Jogos 4
# Campo Minado / Movimento
#
# Usage:
# > python3 Input04PJ04_c.py
#
# v.3.022
# 20180110 / 20230707
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import os, sys, pygame
from pygame.locals import *
import random
import time


# load image function
def load_image(file):
    path = os.path.join('images/minefield', file)
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
        # the displacement vector between each frame
        self.vector = (2, 0)

    def move(self):
        # movement rules
        self.pos.left += self.vector[0]
        self.pos.top += self.vector[1]
        if self.pos.left > 640:
            self.pos.left = 0
        if self.pos.left < 0:
            self.pos.left = 640
        if self.pos.top > 480:
            self.pos.top = 230
        if self.pos.top < 230:
            self.pos.top = 480

    def control(self):
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            self.vector = (0, 0)
        if keys[K_RIGHT]:
            self.vector = (2, 0)
        if keys[K_LEFT]:
            self.vector = (-2, 0)
        if keys[K_UP]:
            self.vector = (0, -2)
        if keys[K_DOWN]:
            self.vector = (0, 2)
        if keys[K_RIGHT] and keys[K_UP]:
            self.vector = (2, -2)
        if keys[K_LEFT] and keys[K_UP]:
            self.vector = (-2, -2)
        if keys[K_RIGHT] and keys[K_DOWN]:
            self.vector = (2, 2)
        if keys[K_LEFT] and keys[K_DOWN]:
            self.vector = (-2, 2)


# paratrooper
class Paratrooper(object):
    """Define a paratrooper, its initial and final position, and state (0: on air, 1: on ground, 2:rescued)"""
    def __init__(self):
        self.image = load_image('skydiver.png')
        self.sound = pygame.mixer.Sound('sounds/minefield/Robot_blip.wav')
        self.initial = (random.randint(0, 640), -20)
        self.final = (random.randint(10, 630), random.randint(230, 470))
        self.pos = self.image.get_rect().move(self.initial[0], self.initial[1])
        self.state = 0
        # number of frames between initial and final paratrooper position
        self.duration = 200
        # the more time passes (i.e. frames) the closest to final destination
        self.proximity = 0
        # step sizes
        self.deltax = (self.final[0] - self.initial[0]) / self.duration
        self.deltay = (self.final[1] - self.initial[1]) / self.duration
        # list with all trajectory intermediate positions
        self.trajectory = self.calculatetrajectory()

    def move(self):
        # move closer to the final destination
        if self.proximity < self.duration:
            self.pos = self.image.get_rect().move(self.trajectory[self.proximity])
            self.proximity += 1
        # move to final destination
        elif self.state != 2:
            self.state = 1
            self.pos = self.image.get_rect().move(self.final[0], self.final[1])

    def calculatetrajectory(self):
        trajectoryfloat = []
        # first position is the initial position
        previouspos = self.initial
        trajectoryfloat.append(previouspos)
        # append a tuple (float x, float y) for each frame with the delta steps
        for i in range(0, self.duration):
            newpos = (previouspos[0] + self.deltax, previouspos[1] + self.deltay)
            trajectoryfloat.append(newpos)
            previouspos = newpos
        # calculate a new trajectory list with tuples (int x, int y), and return it
        trajectoryint = [(int(i[0]), int(i[1])) for i in trajectoryfloat]
        return trajectoryint


# paratrooperlist
class Paratrooperlist(object):
    def __init__(self):
        self.platoon = []

    def release(self):
        # release a new paratrooper if platoon is empty or if last paratrooper has landed
        if len(self.platoon) == 0 or (len(self.platoon) < 10 and self.platoon[-1].state > 0):
            self.platoon.append(Paratrooper())

    def rescue(self, tnk):
        rescued = 0
        for i in [a for a in self.platoon if a.state < 2]:
            if i.pos.colliderect(tnk.pos):
                i.state = 2
                rescued += 1
                i.sound.play()
        return rescued


# mine
class Landmine(object):
    def __init__(self):
        self.image = load_image('explosion2.png')
        self.sound = pygame.mixer.Sound('sounds/minefield/Grenade_Explosion.wav')
        self.pos = self.image.get_rect().move(random.randint(10, 630), random.randint(230, 430))
        self.posinternal = Rect(self.pos.x+15, self.pos.y+15, 20, 20)
        # state: 0=hidden, 1=shown
        self.state = 0

    def fire(self, tnk):
        if self.posinternal.colliderect(tnk.pos):
            self.state = 1


# write text
def writetext(font, text):
    a = font.render(text, 0, (0, 0, 0))
    return a


# event loop
def eventloop(scr, fnt, tnk, prt, sco, min):
    # arguments: scr=screen, fnt=font, tnk=tank, prt=paratrooper list, sco=score, min=mine
    a = 1
    while a == 1:
        # quit gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[K_q]:
                sys.exit()
        # check tank controls
        tnk.control()
        # release a paratrooper
        prt.release()
        # blit the background to erase the last paratrooper position
        [scr.area.blit(scr.image, i.pos, i.pos) for i in prt.platoon]
        # blit the background to erase the last tank position
        scr.area.blit(scr.image, tnk.pos, tnk.pos)
        # move tank
        tnk.move()
        # move paratrooper
        prt.platoon[-1].move()
        # rescue and calculate score
        sco += prt.rescue(tnk)
        # blit paratroopers in new position
        [scr.area.blit(i.image, i.pos) for i in prt.platoon if i.state < 2]
        # blit tank in new position
        scr.area.blit(tnk.image, tnk.pos)
        # write text
        scr.area.blit(scr.image, (120, 5, 50, 30), (120, 5, 50, 30))
        scr.area.blit(writetext(fnt, 'Paratroopers: {}'.format(sco)), (10, 10))
        # blit mine
        # scr.area.blit(min.image, min.pos)
        # test mine
        min.fire(tnk)
        if min.state == 1:
            # blit mine
            scr.area.blit(min.image, min.pos)
            min.sound.play()
            pygame.display.flip()
            time.sleep(5)
            a = 0
        # refresh display
        time.sleep(0.05)
        pygame.display.flip()


# main routine
def main():
    print('\n ::: Input 04 - Campo Minado :::\n\n       Press [Q] to quit.\n')
    # start Pygame
    pygame.init()
    pygame.mixer.init()
    chicago = pygame.font.Font('./fonts/Chicago Normal.ttf', 16)
    score = 0
    # start the display
    screen = Setupscreen('desert640.png')
    # creates tank at initial position
    thetank = Tank(50, 300)
    # creates a paratrooper list
    parat1 = Paratrooperlist()
    # hide a mine
    mine = Landmine()
    # start the event loop with tank moving right
    eventloop(screen, chicago, thetank, parat1, score, mine)


# execute main
if __name__ == '__main__': 
    main()


