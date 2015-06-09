# INPUT
# Código de Máquina 2
#
# Um programa para todas as bases

# Implementacao em Python by RN

# v2.0018
# 20150609

import math

class ConvertBase(object):
    def __init__(self, base, num):
        self.base = int(base)
        self.num = '{}'.format(num).upper()
        self.possible = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[0:self.base]
        self.verbose()
    
    def verbose(self):
        print('-------------------------------------')
        print('           Convert Base')
        print('-------------------------------------')
        print('Base: {}'.format(self.base))
        print('Possible values: {}'.format(self.possible))
        print('Number: {}'.format(self.num))
        # print('Is valid: {}'.format(self.validateNum()))
        print('Number equals to: {}'.format(self.convert()))
        # [print(i, self.digitValue(i)) for i in self.num]

    def validateNum(self):
        for i in self.num:
            if i not in self.possible:
                return False
        return True

    def digitValue(self, d):
        if ord(d) < 58:
            return ord(d)-48
        else:
            return ord(d)-55

    def convert(self):
        if self.validateNum():
            a = 0
            b = [i for i in self.num]
            b.reverse()
            for d in range(0, len(b)):
                a = a + (self.digitValue(b[d]) * pow(self.base, d) )
            return a
        else:
            return 'Cannot convert'


def main():
    a = input('Enter Base (up to 36) : ')
    b = input('Enter Number : ')
    if int(a) <= 36:
        ConvertBase(a, b)


if __name__ == '__main__':
    main()
