# INPUT
# Código de Máquina 2
#
# Um programa para todas as bases

# Implementacao em Python by RN

# v2.0014
# 20150609

import math

class ConvertBase(object):
	def __init__(self, base, num):
		self.base = int(base)
		self.num = '{}'.format(num)
		self.possible = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[0:self.base]
		print(self.possible)

	def convert(self, num):
		pass


def main():
	a = input('Informe a Base (até 36) : ')
	if int(a) <= 36:
		ConvertBase(a, 1)


if __name__ == '__main__':
	main()
	