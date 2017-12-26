# INPUT
# Programação de Jogos 4
#
# Campo Minado / Movimento

# Implementação em Python by RN - now using pygame/pgzero
# Usage:
# >pgzrun Input04PJ04_b.py

# v2.047
# 20171226

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

# define skydiver
skydiver = Actor('skydiver')
# define skydiving
skydiving = 0
skydinitial = (random.randint(10, 630), 10)
skydfinal = (random.randint(10,630), random.randint(180,470))

# movement function
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

def skydive():
    global skydiving
    global skydfinal
    global anim
    # if skydiving is zero, throw another skydiver
    if skydiving == 0:
        anim = animate(skydiver, pos=landingspot())
        skydiving = 1
    skydiver.draw() 
    # if anim.running == False:
    #     skydiving = 0

def landingspot():
    return (random.randint(10,630), random.randint(180,470))

# draw screen
def draw():
    # screen
    screen.fill((255,200,0))
    # ground
    screen.draw.line((0,180), (640,180), (0,0,0))
    # sky
    screen.draw.filled_rect(Rect((0,0), (640,180)), (0,240,255))
    # start
    skydiver.draw()
    tank.draw()

def update():
    # movement
    tankmove()
    skydive()




