# v2.056
# 20171226

import random

# test
# define screen size
WIDTH = 640
HEIGHT = 480

# if skydiverlist is (empty, skydiver skydiver landed), drop skydiver
# drop skydiver
# create skydiver, randomise start/end
# tests if last animation is finished

# drop and landing position
def dropspot():
    return (random.randint(10, 630), 10)

def landingspot():
    return (random.randint(10,630), random.randint(180,470))

# define skydiver
# skyd1 = Actor('skydiver', center=dropspot())
# skyd2 = Actor('skydiver', center=dropspot())
# skyd3 = Actor('skydiver', center=dropspot())
# skyd4 = Actor('skydiver', center=dropspot())
# skyd5 = Actor('skydiver', center=dropspot())
skydiverlist = []
[skydiverlist.append(Actor('skydiver', center=dropspot())) for i in range(0,10)]
# targets
targetlist = []
[targetlist.append(landingspot()) for i in range(0,10)]
# zip
goals = zip(skydiverlist, targetlist)
# parachuter queue
queue = 0

def nextinline():
    global queue
    if queue < 9:
        queue += 1

# skydive
def skydive():
    global skydiverlist
    global targetlist
    global goals
    global queue
    # [animate(i[0], pos=i[1]) for i in goals]
    a = animate(skydiverlist[queue], pos=targetlist[queue])
    a.on_finished = nextinline()
    # if a.running == False:
    #     a.stop()
    #     nextinline()

# drop
def drop():
    global queue
    global skydiverlist
    skydiverlist[queue].draw()

# skydiver: (actor, startpos, endpos)
# skydiverlist = []


# landing variable
# landing = 1

# skydiver = Actor('skydiver')
# skydiver.center = (100,100)

# dropping
# def drop():
#     global skydiverlist
#     if len(skydiverlist) < 5:
#         createskyd()

# landing = landingspot()

# create skydiver
def createskyd():
    global skydiverlist
    skyd1 = Actor('skydiver', center=dropspot())
    skyd2 = Actor('skydiver', center=dropspot())
    skyd3 = Actor('skydiver', center=dropspot())
    skyd4 = Actor('skydiver', center=dropspot())
    skyd5 = Actor('skydiver', center=dropspot())
    skyd1.draw()
    skyd2.draw()
    skyd3.draw()
    skyd4.draw()
    skyd5.draw()

    # skydiverlist.append((Actor('skydiver'), dropspot(), landingspot()))
    # skydiverlist[-1][0].center = skydiverlist[-1][1]
    # skydiverlist[-1][0].draw()
    # animate(skydiverlist[-1][0], skydiverlist[-1][2])
    # print(skydiverlist)
    # print(skydiverlist[-1])

# for i in range(0,10):
#     skydiverlist.append((Actor('skydiver'), dropspot(), landingspot()))
#     skydiverlist[-1][0].draw()

def draw():
    # screen
    screen.fill((255,255,0))
    # skydiver.draw()
    # skyd1.draw()
    # skyd2.draw()
    # skyd3.draw()
    # skyd4.draw()
    # skyd5.draw()
    global skydiverlist
    [i.draw() for i in skydiverlist]
    # drop()

def update():
    # drop()
    # createskyd()
    # drop()
    skydive()