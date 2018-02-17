#################################################
#                   INPUT 8
# Programacao de Jogos 7
# Maze 2 - Treasure Hunt
# UK : Input 7
# Usage:
# > python3 Input08PJ07.py
#
# v2.151
# 20180217
# https://en.wikipedia.org/wiki/Maze_generation_algorithm
# Recursive Backtracker
#################################################
__author__ = 'Rodrigo Nobrega'


# import
import os, sys, pygame
from pygame.locals import *
import numpy as np
import random
# import math


# Global variables
BLACK = (0, 0, 0)
BACKGROUND = (230, 230, 230)
PIXELCOLOR = (255, 192, 128)
BORDER = (255, 128, 128)


# load image function
def load_image(file):
    path = os.path.join('images/maze', file)
    return pygame.image.load(path).convert_alpha()


# write text
def writetext(font, text, colour):
    # colour: tuple (r, g, b)
    a = font.render(text, 0, colour)
    return a


# screen
class Screen(object):
    """Starts a screen and displays background"""
    def __init__(self, image_file=None):
        # physical parameters
        self.size = (1024, 576)
        self.bgcolour = BACKGROUND
        # the canvas
        self.display = pygame.display.set_mode(self.size)
        self.title = pygame.display.set_caption('Treasure Hunt')
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


# The Maze
class Maze(object):
    def __init__(self):
        # block size
        self.bs = 20
        # number of columns in x and y
        self.nx = int(1024/self.bs)
        self.ny = int(546/self.bs)
        # dim p - p is the maze
        self.p = np.zeros((self.nx, self.ny), dtype=int)
        # current position, last position
        self.x = random.randint(1, self.nx-2)
        self.y = random.randint(1, self.ny-2)
        # directions
        self.direction = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
        # stack
        self.stack = []
        # add first cell
        self.record()
        # iterate
        while len(self.stack) > 0:
            self.move()

    def record(self):
        self.p[self.x, self.y] = 1
        self.stack.append((self.x, self.y))

    def neighbours(self, ax, ay):
        return [(ax + self.direction[n][0], ay + self.direction[n][1]) for n in self.direction
                if 0 < ax + self.direction[n][0] < self.nx and 0 < ay + self.direction[n][1] < self.ny]

    def unvisited(self, neigh):
        return [(n[0], n[1]) for n in neigh if self.p[n[0], n[1]] == 0]

    def move(self):
        # calculate potential moves
        potential = self.unvisited(self.neighbours(self.x, self.y))
        # calculate if potentials have unvisited neighbours
        goodmoves = [(i[0], i[1]) for i in potential if len(self.unvisited(self.neighbours(i[0], i[1]))) > 2]
        # now pick the choice
        if len(goodmoves) > 0:
            choice = random.choice(goodmoves)
            self.x = choice[0]
            self.y = choice[1]
            self.record()
        else:
            choice = self.stack.pop()
            self.x = choice[0]
            self.y = choice[1]

    def draw(self, scr):
        for i in range(1, self.nx):
            for j in range(1, self.ny):
                if self.p[i, j] == 1:
                    pygame.draw.rect(scr.display, PIXELCOLOR, (i * self.bs, (j * self.bs) + 30, self.bs, self.bs), 0)
                else:
                    pygame.draw.rect(scr.display, BORDER, (i * self.bs, (j * self.bs) + 30, self.bs, self.bs), 0)


# The Treasure
class Treasure(object):
    def __init__(self):
        # treasure
        self.image = load_image('treasure.png')
        self.pos = self.image.get_rect()
        # start positioning it on the wall
        self.x = 0
        self.y = 0

    def place(self, maz: Maze, scr: Screen):
        # wall position
        r = (0, 0)
        # randomize position until falling in the maze (i.e. outside the wall)
        while maz.p[r[0], r[1]] == 0:
            r = (random.randint(1, maz.nx-2), random.randint(1, maz.ny-2))
        # new position, and draw
        self.x = r[0]
        self.y = r[1]
        self.pos = (self.x * 20, self.y * 20 + 30)
        scr.display.blit(self.image, self.pos)


# The Pirate player


# event loop
def eventloop(scr, fnt, clk, maz, tre):
    # arguments: scr=screen, fnt=font, clk=clock, maz=labirinth, tre=treasure
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
    print('\n ::: Maze :::\n\n       Press [Q] to quit.\n')
    # start Pygame
    pygame.init()
    pygame.mixer.init()
    font1 = pygame.font.Font('./fonts/Chicago Normal.ttf', 16)
    clock = pygame.time.Clock()
    # score = 0
    # start the display
    screen = Screen()
    # creates the Labirinth
    maze = Maze()
    maze.draw(screen)
    # add the Treasure
    treasure = Treasure()
    treasure.place(maze, screen)
    # start the event loop
    eventloop(screen, font1, clock, maze, treasure)


# execute main
if __name__ == '__main__': 
    main()


