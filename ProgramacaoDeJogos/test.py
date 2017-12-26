# v2.048
# 20171226

import random

# test
# define screen size
WIDTH = 640
HEIGHT = 480

# define skydiver
skydiverlist = []

# if skydiverlist is (empty, skydiver skydiver landed), drop skydiver
# drop skydiver
# create skydiver, randomise start/end
# tests if last animation is finished

skydiver = Actor('skydiver')
skydiver.center = (100,100)

def landingspot():
    return (random.randint(10,630), random.randint(180,470))

landing = landingspot()



def draw():
    # screen
    screen.fill((255,255,0))
    skydiver.draw()

def update():
    animate(skydiver, pos=landing)