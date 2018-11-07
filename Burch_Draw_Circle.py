##turtle grapics library##
from turtle import Turtle
##import math library
import math

def main():
    ##Get user input for x##
    x = int(input("Please enter a value for the x coordinate: " + " "))
    ##Get user intput for y##
    y = int(input("Please enter a value for the y coordinate: " + " "))
    ##get user input for radius##
    rad = int(input("Please enter a value for the radius: " + " "))
    ##pass values to be drawn
    drawPolygon(x,y,rad)
    
def drawPolygon(x,y,rad):
    ##use distance formula as parameter##
    distance= 2*math.pi*rad/120
    t =Turtle()
    t.up()
    ##start point##
    t.goto(x+rad,y)
    t.left(90)
    t.down()
    ##draw
    for side in range(120):
        t.left(3)
        t.forward(distance)
  
main()

 
    
    
    