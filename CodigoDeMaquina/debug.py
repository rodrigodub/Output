
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
        #b = input('?')
        while div >= self.base:
            up = div
            div = int( up / self.base )
            remainder = up % self.base
            resultlist.append(remainder)
            #b = input('?')
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
    a = ConvertDecToBase(2, 19)
    a.verbose()


if __name__ == '__main__':
    main()

