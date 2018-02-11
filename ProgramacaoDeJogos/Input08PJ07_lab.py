#################################################
#                   INPUT 8
# Programacao de Jogos 7
# Labirinth 2 - Treasure Hunt
# UK : Input 7
# Usage:
# > python3 Input08PJ07.py
#
# v2.142
# 20180211
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
        self.ny = int(576/self.bs)
        # dim p - p is the labirinth
        self.p = np.zeros((self.nx, self.ny), dtype=int)
        # self.p = np.zeros((self.nx + 5, self.ny + 5), dtype=int)
        # draw border
        self.border()
        # coordinates
        self.x = 1
        self.y = 1
        #self.x = 2
        #self.y = 2
        # last coordinates
        self.lx = 1
        self.ly = 1
        #self.lx = 2
        #self.ly = 2
        # maze positions
        self.j = 0
        self.g = 0
        # create maze
        self.createmaze1()


    def border(self):
        for j in range(0, self.nx):
            self.p[j, self.ny-1] = 6
            self.p[j, 0] = 6
        for j in range(0, self.ny):
            self.p[0, j] = 6
            self.p[self.nx-1, j] = 6

    def createmaze1(self):
        self.j = random.randint(0, 3)
        self.g = self.j
        self.createmaze2()

    def createmaze2(self):
        self.y = self.ly + 2 * ((self.j == 0) - (self.j == 2))
        self.x = self.lx + 2 * ((self.j == 3) - (self.j == 1))
        if self.x > self.nx-1:
            self.x -= self.nx
        if self.y > self.ny-1:
            self.y -= self.ny
        try:
            self.p[self.x, self.y]
        except IndexError:
            self.createmaze3()
        if self.p[self.x, self.y] == 0:
            self.p[self.x, self.y] = self.j+1
            self.p[int((self.x + self.lx) / 2), int((self.y + self.ly) / 2)] = 5
            self.lx = self.x
            self.ly = self.y
            self.createmaze1()
        else:
            self.createmaze3()

    def createmaze3(self):
        self.j = (self.j + 1) % 4
        if self.j != self.g:
            self.createmaze2()
        else:
            self.createmaze4()

    def createmaze4(self):
        try:
            self.j = self.p[self.lx, self.ly] - 1
            self.p[self.lx, self.ly] = 5
        except IndexError:
            print('Index Error')
        if self.j < 4:
            self.lx = self.lx - 2 * ((self.j == 3) - (self.j == 1))
            self.ly = self.ly - 2 * ((self.j == 0) - (self.j == 2))
            self.createmaze1()
        else:
            self.createmaze5()

    def createmaze5(self):
        for cnt in range(0, 21):
            self.p[2 + 2 * random.randint(0, int((self.nx - 3)/2)), 1 + random.randint(0, (self.ny - 3))] = 5
            self.p[1 + random.randint(0, (self.nx - 3)), 2 + 2 * random.randint(0, int((self.ny - 3)/2))] = 5


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


