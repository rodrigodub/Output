#################################################
#                   INPUT 8
# Programacao de Jogos 7
# Labirinth 2 - Treasure Hunt
# UK : Input 7
# Usage:
# > python3 Input08PJ07.py
#
# v2.148
# 20180213
# trying https://en.wikipedia.org/wiki/Maze_generation_algorithm
# Recursive Backtracker
#################################################
__author__ = 'Rodrigo Nobrega'

import numpy as np
import random

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
        self.lx = self.x
        self.ly = self.y
        # directions
        self.direction = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
        # initial direction
        # self.turn = random.choice('NSEW')
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
        return [(ax + self.direction[n][0], ay + self.direction[n][1]) for n in self.direction]

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

        # new cell position
        # self.x += self.direction[self.turn][0]
        # self.y += self.direction[self.turn][1]
        # # test if in range, otherwise use last position
        # if self.x in range(0, self.nx) and self.y in range(0, self.ny):
        #     # test if unvisited neighbours, otherwise pop last
        #     if self.p[self.x, self.y] == 0:
        #         self.record()
        #     else:
        #         a = self.stack.pop()
        #         self.x = a[0]
        #         self.y = a[1]
        # else:
        #     self.x = self.lx
        #     self.y = self.ly
        # self.lx = self.x
        # self.ly = self.y
        # self.turn = random.choice('NSEW')


# main routine
def main():
    print('\n ::: Labirinth :::\n\n::::::::::::::::::::::::::::::::::::::::::::\n')
    lab = Maze()
    print('Block Size [BS]: {}\nNumber of columns [NX]: {}\nNumber of lines [NY]: {}'
          .format(lab.bs, lab.nx, lab.ny))
    print('\n')
    print('P[] size: {} cols X {} lins'.format(len(lab.p[0]), len(lab.p)))
    print(lab.p)
    print('\n::::::::::::::::::::::::::::::::::::::::::::\n')


# execute main
if __name__ == '__main__':
    main()


