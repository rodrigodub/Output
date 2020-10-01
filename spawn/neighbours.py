# coding: utf-8
print('PyDev console: using IPython 7.14.0\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/Users/rodrigo/Code/Output/spawn'])
from spawn import *
bo = Environment(5,5,1)
bo.grid
bo = Environment(10,10,1)
bo.grid
a1 = bo.grid.copy()
a1
b1 = a1.copy()
bo.neighbours(9,5,b1)
bo.neighbours(9,6,b1)
a1[9]
[bo.neighbours(9, i, b1) for i in a1[9]]
[bo.neighbours(8, i, b1) for i in a1[8]]
a1[8]
a1
a1[0]
b1[0]
[bo.neighbours(0, i, b1) for i in a1[0]]
bo.lines
bo.columns
a1[0]
a1=b1
bo.grid
a1 = bo.grid.copy()
b1 = bo.grid.copy()
a1 == b1
a1[9]
a1[9]
a1[10]
a1[9]
a1[0]
a1[:,0]
a1[:,0:2]
a1[:,0:3]
bo.neighbours(0,0,b1)
bo.neighbours(0,0,a1)
[bo.neighbours(0,i,a1) for i in a1[0]]
[bo.neighbours(0,i,a1) for i in range(a1.shape[0])]
a1
[bo.neighbours(9,i,a1) for i in range(a1.shape[0])]
a1
a2 = np.array([a1[-1]])
a2
a2 = np.array([a1[-1], a1])
a2 = np.array([a1[-1], a1[:,:]])
a1
a2 = np.vstack([a1[0], a1])
a2
a3 = np.vstack([a2, a1[-1]])
a3
a3[:,0]
a3[:,-1]
a4 = np.column_stack([a3[:,0], a3])
a4
a5 = np.column_stack([a4, a3[:,-1]])
a5
a5
a1
a1.shape()
a1.shape
a5.shape
a1 == a5[1:-1, 1:-1]
a1 == a5
['hey' for i in a1]
a1
b1
a5
for li in range(a1.shape[0]):
    for co in range(a1.shape[1]):
        b1[li, co] = 0
        b1[li, co] += a5[li-1, co-1]
        b1[li, co] += a5[li - 1, co]
        b1[li, co] += a5[li - 1, co + 1]
        b1[li, co] += a5[li, co - 1]
        b1[li, co] += a5[li, co + 1]
        b1[li, co] += a5[li + 1, co - 1]
        b1[li, co] += a5[li + 1, co]
        b1[li, co] += a5[li + 1, co + 1]
        
b1
b1.shape
a5
for li in range(a1.shape[0]):
    for co in range(a1.shape[1]):
        b1[li, co] = 0
        b1[li, co] += a5[li, co]
        b1[li, co] += a5[li, co+1]
        b1[li, co] += a5[li, co+2]
        b1[li, co] += a5[li+1, co]
        b1[li, co] += a5[li+1, co+2]
        b1[li, co] += a5[li+2, co]
        b1[li, co] += a5[li+2, co+1]
        b1[li, co] += a5[li+2, co+2]
        
b1
get_ipython().run_line_magic('save', 'neighbours.py')
