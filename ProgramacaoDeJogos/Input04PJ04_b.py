# INPUT
# Programação de Jogos 4
#
# Campo Minado / Movimento

# Implementação em Python by RN - now using pygame/pgzero
# Usage:
# >pgzrun Input04PJ04_b.py

# v2.0038
# 20171224


# define screen size
WIDTH = 640
HEIGHT = 480
# initial tank position
tankposx = 320
tankposy = 120
tankdx = 2
tankdy = 0

# define tank and its position
tank = Actor('tank2')
tank.center = (tankposx, tankposy)

# movement function
def tankmove():
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
        tankposy = 220
    if tankposy > 219:
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




