# INPUT
# Programação de Jogos 4
#
# Campo Minado / Movimento

# Implementação em Python by RN - now using pygame/pgzero
# Usage:
# >pgzrun Input04PJ04_b.py

# v2.0037
# 20171224


# define screen size
WIDTH = 640
HEIGHT = 480
# initial tank position
tankpos = (320, 120)

# define tank and its position
tank = Actor('tank2')
tank.center = tankpos

# movement function
def move():
    pass

# draw screen
def draw():
    screen.fill((255,200,0))
    screen.draw.line((0,240), (640,240), (0,0,0))
    tank.draw()

def update():
    # movement
    if keyboard.right:
        tank.left += 2
        if tank.left > WIDTH:
            tank.left = 0
    if keyboard.up:
        tank.top -= 2
        if tank.bottom < 0:
            tank.bottom = 239
    if keyboard.left:
        tank.right -= 2
        if tank.right < 0:
            tank.right = 640
    if keyboard.down:
        tank.bottom += 2
        if tank.bottom > 239:
            tank.top = 0




