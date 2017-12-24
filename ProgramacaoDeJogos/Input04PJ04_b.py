# INPUT
# Programação de Jogos 4
#
# Campo Minado / Movimento

# Implementação em Python by RN - now using pygame/pgzero
# Usage:
# >pgzrun Input04PJ04_b

# v2.0034
# 20171224


# define screen size
WIDTH = 640
HEIGHT = 480

# define tank and its position
tank = Actor('tank2')
tank.topright = (20, 100)

# draw screen
def draw():
    screen.fill((255,200,0))
    screen.draw.line((0,240), (640,240), (0,0,0))
    tank.draw()

def update():
    tank.left += 2
    if tank.left > WIDTH:
        tank.left = 0


