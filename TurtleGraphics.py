#TurtleGraphics.py
#Name: Cameron Sailors
#Date: 2/16/2025
#Assignment: Concentric Squares

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
        
def drawPolygon(myTurtle, sides):
    for i in range(sides):
        myTurtle.forward(50)
        myTurtle.right(360/sides)

def fillCorner(myTurtle, corner):
    myTurtle.penup()
    myTurtle.goto(-200,200)
    myTurtle.pendown()
    
    drawSquare(myTurtle,400)
    
    if corner == 1:
        myTurtle.begin_fill()
        drawSquare(myTurtle,200)
        myTurtle.end_fill()
    elif corner == 2:
        myTurtle.forward(200)
        myTurtle.begin_fill()
        drawSquare(myTurtle,200)
        myTurtle.end_fill()
    elif corner == 3:  
        myTurtle.right(90)
        myTurtle.forward(200)
        myTurtle.left(90)
        myTurtle.begin_fill()
        drawSquare(myTurtle,200)
        myTurtle.end_fill()
    elif corner == 4:
        myTurtle.forward(400)
        myTurtle.right(90)
        myTurtle.forward(400)
        myTurtle.right(90)
        myTurtle.begin_fill()
        drawSquare(myTurtle,200)
        myTurtle.end_fill()
        
def squaresInSquares(myTurtle,num):
    
    scale = 50
    
    for i in range(num):
        for j in range(4):
            myTurtle.pendown()
            myTurtle.forward(scale*i)
            myTurtle.right(90)
        myTurtle.penup()
        myTurtle.setpos(myTurtle.xcor()-scale/2,myTurtle.ycor()+scale/2)

        
        
def main():
    myTurtle = turtle.Turtle()
    
   # drawSquare(myTurtle,100)
   
   # drawPolygon(myTurtle, 5) #draws a pentagon
   # drawPolygon(myTurtle, 8) #draws an octogon

   # fillCorner(myTurtle, 4) #draws a square with top right corner filled in.
   # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
   # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
