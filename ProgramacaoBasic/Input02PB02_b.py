# INPUT
# Programacao BASIC 02
#
# A arte de fazer laços
#
# Pôr do sol

# Implementacao em Python by RN
# Using Pillow
#
# references:
# https://pillow.readthedocs.org/reference/Image.html
# https://pillow.readthedocs.org/handbook/concepts.html#concept-modes
# http://www.w3schools.com/html/html_colornames.asp

# v2.0011
# 20150606

from PIL import Image, ImageDraw
import random


class Screen(object):
    def __init__(self, width, height):
        self.colors = ['Black', 'Lime', 'Yellow', 'Blue', 'Red', 'White', 'Cyan', 'Magenta', 'Orange']
        self.screen = Image.new('RGB', (width, height), 'Black')
        self.draw = ImageDraw.Draw(self.screen)


class Sunset(object):
    def __init__(self, tela):
        self.sun(tela)
        self.horizon(tela)

    def sun(self, tela):
        for n in range(0, 80):
            tela.draw.line([(320, 160), (640-random.randint(0,640), 160-random.randint(0,160))]
                , tela.colors[2])

    def horizon(self, tela):
        for n in range(160, 320, 25):
            tela.draw.line([(320, 160), (0, n)], tela.colors[4])
            tela.draw.line([(320, 160), (640, n)], tela.colors[4])
        for n in range(0, 640, 20):
            tela.draw.line([(320, 160), (n, 320)], tela.colors[4])


def main():
    a = Screen(640, 320)
    Sunset(a)
    a.screen.show()


if __name__ == '__main__':
    main()