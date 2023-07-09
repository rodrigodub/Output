# set screen width and height
WIDTH = 800
HEIGHT = 250

# create the back layer
layer_back = Actor('rn_mountains_far')
layer_back.topleft = 0, 0
layer_back.speed = 1

#create the middle layer
layer_middle = Actor('rn_mountains_middle')
layer_middle.topleft = 0, 100
layer_middle.speed = 2

#create the front layer
layer_front = Actor('rn_mountains_near')
layer_front.topleft = 0, 180
layer_front.speed = 3

#add layers to list
layers = [layer_back, layer_middle, layer_front]

def update():
    for l in layers:
        # move each layer to the left
        l.left -= l.speed
        # if the layer has moved far enough to the left
        # then reset the layers position
        if l.right <= WIDTH:
            l.left = 0

def draw():
    screen.clear()
    # draw all images in the image list
    for l in layers:
        l.draw()