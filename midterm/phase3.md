Phase 3

What We Did:

In Phase 3, we turned our processing sketches into functions.

How I did it:

I took my original code:

def setup():
    size(150, 150)
    noStroke()

def draw():
    fill(0)
    rect(40, 70, 60, 10)
    rect(50, 40, 40, 40)
    ellipse(70, 80, 30, 30)

From here, I expanded my canvas:

def setup():
    size(400, 400)
    noStroke()

At this point, I plugged my shapes into the given function:

def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(0)
    rect(40, 70, 60, 10)
    rect(50, 40, 40, 40)
    ellipse(70, 80, 30, 30)
    pop()

After adding on the final given function, my total code became:

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
