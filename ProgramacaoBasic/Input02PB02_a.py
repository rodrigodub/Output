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

# v2.0006
# 20150605

from PIL import Image

class Tela(object):
	def __init__(self):
		self.tela = Image.new('RGB', (640,320), 'Black')
		self.tela.show()



def main():
	Tela()


if __name__ == '__main__':
	main()