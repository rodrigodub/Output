# INPUT
# Programação de Jogos 4
#
# Campo Minado / Movimento

# Implementação em Python by RN - now using pygame/pgzero
# Usage:
# >pgzrun Input04PJ04_b.py

# v.3.022
# 20171227 / 20230707

import random

# define screen size
WIDTH = 640
HEIGHT = 480
# initial tank position
tankposx = 20
tankposy = 360
tankdx = 2
tankdy = 0

# define tank and its position
tank = Actor('tank4')
tank.center = (tankposx, tankposy)

# drop and landing position
def dropspot():
    return (random.randint(10, 630), -20)

def landingspot():
    return (random.randint(10,630), random.randint(180,470))

# define skydivers
skydiverlist = []
[skydiverlist.append(Actor('skydiver', center=dropspot())) for i in range(0,10)]
# their targets
targetlist = []
[targetlist.append(landingspot()) for i in range(0,10)]
# zip between them
goals = zip(skydiverlist, targetlist)
# parachuter queue
queue = 0

# order of parachuting
def nextinline():
    global queue
    if queue < 9:
        queue += 1

# tank movement function
def tankmove():
    # they're global
    global tankposx
    global tankposy
    global tankdx
    global tankdy
    # monitor keyboard
    if keyboard.right:
        tankdx = 2
        tankdy = 0
    if keyboard.up:
        tankdx = 0
        tankdy = -2
    if keyboard.left:
        tankdx = -2
        tankdy = 0
    if keyboard.down:
        tankdx = 0
        tankdy = 2
    if keyboard.space:
        tankdx = 0
        tankdy = 0
    if keyboard.right and keyboard.up:
        tankdx = 2
        tankdy = -2
    if keyboard.right and keyboard.down:
        tankdx = 2
        tankdy = 2
    if keyboard.left and keyboard.up:
        tankdx = -2
        tankdy = -2
    if keyboard.left and keyboard.down:
        tankdx = -2
        tankdy = 2    
    # define new position
    tankposx += tankdx
    tankposy += tankdy
    # test limits
    if tankposx < 0:
        tankposx = 640
    if tankposx > 640:
        tankposx = 0
    if tankposy < 180:
        tankposy = 480
    if tankposy > 480:
        tankposy = 180
    # draw
    tank.center = (tankposx, tankposy)

# skydiving
def skydive():
    global skydiverlist
    global targetlist
    # global goals
    global queue
    a = animate(skydiverlist[queue], pos=targetlist[queue], tween='linear', duration=1.5)
    if targetlist[queue][1] - skydiverlist[queue].y < 100 :
        nextinline()
    # return (skydiverlist[queue].center, targetlist[queue])

# draw screen
def draw():
    # screen
    screen.fill((255,200,0))
    # ground
    screen.draw.line((0,180), (640,180), (0,0,0))
    # sky
    screen.draw.filled_rect(Rect((0,0), (640,180)), (0,240,255))
    # start
    global skydiverlist
    [i.draw() for i in skydiverlist]
    tank.draw()

def update():
    # movement
    tankmove()
    skydive()




