Power Assignment

What We Did:
In this assignment we were assigned the task of creating a right-facing parabola using the following template:

def print_graph(n):

def get_power(x, n):

for i in range(-8, 9):

What I knew:

Before starting my programming, I thought about what I knew I would do going into this assignment. I knew that I had to use the get_power function to plug into the print_graph function, and I knew that given the print_graph function's print() output, this print_graph function would also end up being the closer of my program. I would use get_power describing the x ** n equation, and then take that output (n) and plug it into my print_graph function, resulting in printing n * '*', such that each row would have a number of asterisks equal to x squared (**2), as shown in the pattern. I also knew that the for i in range would be used to create the varying 'x' inputs, giving me my variation of shape based on which number in the range I'm on.

What I did wrong from here:

While defining my functions, I was trying to nest the get_power function and the for i statement into the print_graph function. This was because I knew that the output of my get_power function ended up being the input for my print_graph function, and that the variable input for my get_power function was the output of the for i statement, which in this case was just the numbers -8 to 8. Here is an example:

def get_power(x, n):
    return x ** n

def print_graph(n):
    for i in range(-8,9):
        print(get_power(i, 2) * '*')

print_graph()

Solutions:

What I was rather stumpped on for maybe ten minutes was the fact that I needed an input for my print_graph, which I couldn't think of a way to successfully connect the output of get_power to print_graph. This is when I decided I needed to simplify things, turning each function definition into a simple equation. I knew that get_power was essentially just an equation, and print_graph took that ouput and multiplies that by a character. Here is what I came up with for my definitions:

def get_power(x, n):
        return x ** n

def print_graph(n):
        print(n * "*")

This way, I could attach the functions to each other such that the direct ouput of each separated part of my program is the input of the next part. I knew that get_power lead into print_graph, and given that for i leads to get_power, I decided to start my call with the for i statement. With the print function on the end of print_graph function, I was able to simply put print_graph with its input as the only function I needed to complete my parabola, and because we know that the input of print_graph is get_power, I put in (i, 2) as the get_power input, giving me a final program of:

def get_power(x, n):
        return x ** n

def print_graph(n):
        print(n * "*")

for i in range(-8, 9):
        print_graph(get_power(i, 2))
