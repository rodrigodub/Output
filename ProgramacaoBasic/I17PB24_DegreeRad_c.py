#################################################
#                   INPUT 17
#
# Programacao Basic 24
# SIN & COS chart
#
# Usage:
# > python I17PB24_DegreeRad_c.py
#
# v.3.029
# 20230723
#
#################################################
__author__ = 'Rodrigo Nobrega'


# import
# libraries
import math
import matplotlib.pyplot as plt
import numpy as np

# create data
# values = np.cumsum(np.random.randn(1000, 1))
sin_values = np.sin(np.arange(0, 4 * math.pi, math.pi / 100))
cos_values = np.cos(np.arange(0, 4 * math.pi, math.pi / 100))

# use the plot function
plt.plot(sin_values, color='skyblue')
plt.plot(cos_values, color='orange')
plt.show()
