# INPUT
# Código de Máquina 2
#
# Um programa para todas as bases

# Implementação em Python by RN

# v2.0021
# 20150610

import math

class ConvertBaseToDec(object):
    """
    Class to convert a number in a given base to its decimal value.
    Arguments:
    base: integer, between 1 and 36
    num: string, representing a number on that base (ex.: 14E in hex)
    """
    def __init__(self, base, num):
        self.base = int(base)
        self.num = '{}'.format(num).upper()
        self.possible = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[0:self.base]
        self.decimal = self.convertToDecimal()
        # self.verbose()
    
    def verbose(self):
        print('-------------------------------------')
        print('      Convert Base to Decimal')
        print('-------------------------------------')
        print('Base: {}'.format(self.base))
        print('Possible values: {}'.format(self.possible))
        print('Number: {}'.format(self.num))
        print('Number equals to: {}'.format(self.decimal))

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

    def convertToDecimal(self):
        if self.validateNum():
            a = 0
            b = [i for i in self.num]
            b.reverse()
            for d in range(0, len(b)):
                a = a + (self.digitValue(b[d]) * pow(self.base, d) )
            return a
        else:
            return 'Cannot convert'


class ConvertDecToBase(object):
    """
    Class to convert a decimal number to its value in a given base.
    Arguments:
    base: integer, between 1 and 36
    num: integer, decimal base
    """
    def __init__(self, base, num):
        self.base = int(base)
        self.num = int(num)
        self.converted = self.convertToBase()
        # self.verbose()

    def verbose(self):
        print('-------------------------------------')
        print('      Convert Decimal to Base')
        print('-------------------------------------')
        print('Decimal: {}'.format(self.num))
        print('Base: {}'.format(self.base))
        print('Number on Base: {}'.format(self.convertToBase()))

    def convertToBase(self):
        resultlist = []
        resultstring = ''
        up = self.num
        # main loop
        div = int( up / self.base )
        remainder = up % self.base
        resultlist.append(remainder)
        while div > self.base:
            up = div
            div = int( up / self.base )
            remainder = up % self.base
            resultlist.append(remainder)
        resultlist.append(div)
        # convert resultlist to string
        resultlist.reverse()
        for i in resultlist:
            if i < 10:
                resultstring += '{}'.format(i)
            else:
                resultstring += '{}'.format(chr(i+55))
        return resultstring


def main():
    a = input('Enter Base (up to 36) : ')
    b = input('Enter Number : ')
    if int(a) <= 36:
        x = ConvertBaseToDec(a, b)
        y = ConvertDecToBase(a, x.decimal)


if __name__ == '__main__':
    main()
