# INPUT
# Programacao BASIC 02
#
# A arte de fazer laços
#
# Pintando o sete e outros números

# Implementacao em Python by RN
# Using Pillow
#
# references:
# https://pillow.readthedocs.org/reference/Image.html
# https://pillow.readthedocs.org/handbook/concepts.html#concept-modes
# http://www.w3schools.com/html/html_colornames.asp

# v2.0008
# 20150605

from PIL import Image, ImageDraw
import random


class Tela(object):
	def __init__(self, width, height):
		self.colors = ['Black', 'Lime', 'Yellow', 'Blue', 'Red', 'White', 'Cyan', 'Magenta', 'Orange']
		self.tela = Image.new('RGB', (width, height), 'Black')
		self.desenho = ImageDraw.Draw(self.tela)
		#self.tela.show()

	def bloco(self, x, y, color):
		self.desenho.rectangle([(x, y), (x+10, y+10)], color)
		#self.tela.show()

	def loop(self):
		for n in range(0,630,10):
			m = random.randint(0, 31) * 10
			c = self.colors[random.randint(0,8)]
			self.bloco(n, m, c)


def main():
	a = Tela(640, 320)
	#a.bloco(100, 100, a.colors[1])
	for i in range(0,50):
		a.loop()
	a.tela.show()



if __name__ == '__main__':
	main()