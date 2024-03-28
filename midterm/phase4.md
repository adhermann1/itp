Phase 4

What we did:

In Phase 4, we took our image and made it a tile function capable of changing scale based on the dimensions of our tile.

How we did it:

First, I knew I had to use our previous function to create the cell:

def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(0)
    rect(40, 70, 60, 10)
    rect(50, 40, 40, 40)
    ellipse(70, 80, 30, 30)
    pop()

This is what would be the base outline for our cells. Next, I needed to change the size of my window so that the pattern would work. My shape essentially follows the dimensions of a 60 by 70 rectangle, so I set my window to 600 by 700 px to accomodate this. This left me with the following functions:

def setup():
    size(600, 700)
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

After this is where I had trouble. I knew that I needed to create my tiles through nested for loops, but I struggled to figure out how to do this. I have solved many problems this semester bu simplifying my thinking, so I did just that. I knew that the ultimate goal was to call my drawObject function, and that I wanted my tiles to follow a square shape. Therefore, I decided to make simple for in range loops for x and y and to set these equal to each other. Then, I knew I had to attach drawObject with coordinates to the end. I came up with this:

def draw():
    for x in range(10):
        for y in range(10):
            drawObject(x,y,1)

When I put this into my Processing, I just got a bunch of Jamiroquai stacked on top of each other. I knew I printed all I needed, I just needed them to spread out. I heard Rachel's words echoe through my mind, "You can multiply the cell width with the current x position in the nested for-loop to position your object in the x-axis. For the y-axis, this will be the cell height multiplied by the current y position."
I multiplied my x and y by 60 and 70 respectively, and I created an actual grid shape. I realized that I needed to get my math on point in order to have my finallized code. I knew that a scale of 1 correlated to a 10x10 grid on a 600x700 grid.
Given this, I knew that my range was essentially my variable, in the sense that this was the singular input for seeing a grid of that dimension. I noticed that I needed to move my shapes more the larger they were, meaning that the smaller my dimensions grow, the larger my x, y and s will have to grow. I figured that going from 10 Jamiroquai to 5 would require I make my x, y and s all double. Observing their relationships with n, therefore, I deduced the simplest fractions to explain their relationships:

def draw():
    for x in range(n):
        for y in range(n):
            drawObject(x*600/n,y*700/n,10/n)

My grid was not complete. I still needed to fine tune some things. I noticed I had an awkward gap at the top of my canvas, and that sometimes my tiles weren't completely fitting in the canvas. I realized that the original coordinates I was using from Phase 3 were not trimmed to fit to the canvas completely, so I adjusted the numbers to properly fit Jamiroquai. This gave me my final code:

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
