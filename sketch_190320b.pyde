def setup():
    frameRate(30)
    rectMode(CORNER)
    size(200,200)
    global x
    global y
    x=0
    y=0
    import random
def draw():
    fill(random(255),random(255),random(255))
    background(0)
    global x
    x=x+1
    global y
    y=y+1
    rect(x,y,50,50)
    if x>width:
        exit()
