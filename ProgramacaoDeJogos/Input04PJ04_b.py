# INPUT
# Programação de Jogos 4
#
# Campo Minado / Movimento

# Implementação em Python by RN - now using pygame/pgzero
# Usage:
# >pgzrun Input04PJ04_b.py

# v2.0039
# 20171225


# define screen size
WIDTH = 640
HEIGHT = 480
# initial tank position
tankposx = 50
tankposy = 50
tankdx = 2
tankdy = 0

# define tank and its position
tank = Actor('tank2')
tank.center = (tankposx, tankposy)

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
    # define new position
    tankposx += tankdx
    tankposy += tankdy
    # test limits
    if tankposx < 0:
        tankposx = 640
    if tankposx > 640:
        tankposx = 0
    if tankposy < 0:
        tankposy = 230
    if tankposy > 230:
        tankposy = 0
    # draw
    tank.center = (tankposx, tankposy)
    

# draw screen
def draw():
    screen.fill((255,200,0))
    screen.draw.line((0,240), (640,240), (0,0,0))
    tank.draw()

def update():
    # movement
    tankmove()




