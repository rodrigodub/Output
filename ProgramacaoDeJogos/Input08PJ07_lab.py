#################################################
#                   INPUT 8
# Programacao de Jogos 7
# Labirinth 2 - Treasure Hunt
# UK : Input 7
# Usage:
# > python3 Input08PJ07.py
#
# v2.138
# 20180206
#################################################
__author__ = 'Rodrigo Nobrega'

import numpy as np

class Maze(object):
    def __init__(self):
        self.bs = 20
        self.nx = int(1024/self.bs)
        self.ny = int(576/self.bs)
        # dim p
        self.p = np.zeros((self.nx, self.ny), dtype=int)
        self.border()

    def border(self):
        for j in range(0, self.nx):
            self.p[j, self.ny-1] = 6
            self.p[j, 0] = 6
        for j in range(0, self.ny):
            self.p[0, j] = 6
            self.p[self.nx-1, j] = 6


# main routine
def main():
    print('\n ::: Labirinth :::\n\n::::::::::::::::::::::::::::::::::::::::::::\n')
    lab = Maze()
    print('Block Size [BS]: {}\nNumber of columns [NX]: {}\nNumber of lines [NY]: {}'
          .format(lab.bs, lab.nx, lab.ny))
    print('\n')
    print('P[] size: {} cols X {} lins'.format(len(lab.p[0]), len(lab.p)))
    print('\n::::::::::::::::::::::::::::::::::::::::::::\n')



# execute main
if __name__ == '__main__':
    main()


