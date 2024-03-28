def setup():
    size(400, 400)
    noStroke()

def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(0)
    rect(40, 70, 60, 10)
    rect(50, 40, 40, 40)
    ellipse(70, 80, 30, 30)
    pop()

def draw():
    drawObject(0,0,1)
    drawObject(0,200,1)
