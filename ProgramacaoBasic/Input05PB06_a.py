#################################################
#                   INPUT
# Programação Basic 6
# O que são variáveis
#
# Usage:
# > python3 Input05PB06_a.py
#
# v2.095
# 20180121
#################################################

import time


def main():
    x = 0
    while True:
        print('{} '.format(x), end='', flush=True)
        time.sleep(.025)
        x += 1


# execute main
if __name__ == '__main__':
    main()