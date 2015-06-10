# INPUT
# Código de Máquina 3
#
# BIN, DEC, HEX

# Implementação em Python by RN

# v2.0022
# 20150610

import math
import Input02CM02_a as conv


def main():
    a = input('Enter Base (up to 36) : ')
    b = input('Enter Number : ')
    if int(a) <= 36:
        x = conv.ConvertBaseToDec(a, b)
        y = conv.ConvertDecToBase(a, x.decimal)
        x.verbose()
        y.verbose()


if __name__ == '__main__':
    main()
