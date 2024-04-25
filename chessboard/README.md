Chessboard Assignment

**Documentation:**

In this assignment, we created a chessboard out of hashes using Javascript that print out a certain size given a number.

I first started with my Bindings. I had to create the size binding, so I simply put let size = 4 as a random number to use. I then created a chess binding to attach my size number to the string. From there, I knew that I wanted to use a loop like I used for the pyramid assignment. I created my for (let i = 0; i < size; i++) and for (let j = 0; j < size; j++) as the dimensions of the chessboard. I decided to start at zero, and I knew that I only wanted my hashes to go up to correlate to the number I put in. I had some trouble trying to figure out how to create the spacing I wanted, but figured I could use even numbers as a differentiator. I initially tried to change this based on just the rows, but I realized I had to use both variables. From there, I figured that there is some relationship with even numbers, and observed the relationship between the hashes coordinates and the spaces coordinates. I used this to state that:   
if ((i + j) % 2 == 0)
    chess += " ";
  else
    chess += "#"

This means that when the coordinates add to an even number, there is a blank space, and when they don't, there is a hash. From here, I added chess += "\n" so that my program would loop for both the rows and columns. Finally, I added the console.log(chess); to print my code.
