def setup():
    size(600, 700)
    noStroke()

def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(0)
    rect(0, 30, 60, 10)
    rect(10, 0, 40, 40)
    ellipse(30, 40, 30, 30)
    pop()

def draw():
    for x in range(n):
        for y in range(n):
            drawObject(x*600/n,y*700/n,10/n)
