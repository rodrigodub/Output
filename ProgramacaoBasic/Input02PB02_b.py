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

# v2.0009
# 20150606

from PIL import Image, ImageDraw
import random


class Screen(object):
	def __init__(self, width, height):
		self.colors = ['Black', 'Lime', 'Yellow', 'Blue', 'Red', 'White', 'Cyan', 'Magenta', 'Orange']
		self.screen = Image.new('RGB', (width, height), 'Black')
		self.draw = ImageDraw.Draw(self.screen)
		#self.screen.show()

	# def square(self, x, y, color):
	# 	self.draw.rectangle([(x, y), (x+10, y+10)], color)
	# 	#self.screen.show()

	# def loop(self):
	# 	for n in range(0,630,10):
	# 		m = random.randint(0, 31) * 10
	# 		c = self.colors[random.randint(0,8)]
	# 		self.square(n, m, c)


class Sunset(object):
	def __init__(self, tela):
		self.sun(tela)

	def sun(self, tela):
		for n in range(0, 80):
			tela.draw.line([(320, 160), (640-random.randint(0,640), 160-random.randint(0,160))]
				, tela.colors[2])


def main():
	a = Screen(640, 320)
	Sunset(a)
	a.screen.show()


if __name__ == '__main__':
	main()