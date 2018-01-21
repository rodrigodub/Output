#################################################
#                   INPUT
# Programação Basic 6
# O que são variáveis
#
# Usage:
# > python3 Input05PB06_a.py
#
# v2.094
# 20180121
#################################################

import time


def main():
    x = 0
    while True:
        print('{} '.format(x))
        time.sleep(.05)
        x += 1


# execute main
if __name__ == '__main__':
    main()