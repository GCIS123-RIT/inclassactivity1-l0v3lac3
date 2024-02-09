""" group members         contribution
   1. Wurist Zewdie       setpos and hexagone functions
   2. Yara   Alhourani    pattern and main functions      
   3.Afifa   Monzur       circle and square functions   
 in this activity we use six functions(setpos,hexagon,circle,square,pattern and main).
     setpos:sets the position of the turle to co-ordinate x and y without leaving any trace
     hexagon:draw a hexagone of 50 units each side filled with hexa_color,and border_color for border.
     square:draws a square of 90 units each side filled with square_color,and border_color border.
     circle:accept turtle object to draw a circle filled with circle_color,and border_color border.
     pattern:draws hexagon filled with hexa_color followed by circle filled with circle_color 
            then square filled with square_color.
     main: contains anyother inputs and call the functions."""

import turtle
turta=turtle.Turtle()     # turta is the variable we use to represent turtle object
def setPos(turta, x, y):
    turta.penup()                 
    turta.setheading(0)
    turta.goto(x, y)
    turta.pendown()

def hexagon(turta, hexa_color, border_color):
    turta.fillcolor(hexa_color)
    turta.pencolor(border_color)
    turta.begin_fill()
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.end_fill()
    turta.penup()
def circle(turta, circle_color, border_color):
    turta.pencolor(border_color)
    turta.fillcolor(circle_color)
    turta.begin_fill()
    turta.circle(50)
    turta.end_fill()

def square(turta, square_color, border_color):
    turta.fillcolor(square_color)
    turta.pencolor(border_color)
    turta.begin_fill()
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.end_fill()


def pattern(hexa_color, square_color, circle_color, border_color):
    setPos(turta,-190,150)
    hexagon(turta, hexa_color, border_color)
    setPos(turta,-100,40)
    hexagon(turta, hexa_color, border_color)
    setPos(turta,-10,-70)
    hexagon(turta, hexa_color, border_color)

    setPos(turta,-45,150)
    circle(turta, circle_color, border_color)
    setPos(turta,45,40)
    circle(turta, circle_color, border_color)
    setPos(turta,135,-70)
    circle(turta, circle_color, border_color)

    setPos(turta,25,150)
    square(turta, square_color, border_color)
    setPos(turta,115,40)
    square(turta, square_color, border_color)
    setPos(turta,205,-70)
    square(turta, square_color, border_color)

def main():
        hexa_color=input("enter the color of hexagon=")
        square_color=input("enter color of square=")
        circle_color=input("enter color of circle=")
        border_color=input("enter border color=")
        pattern(hexa_color, square_color, circle_color, border_color)
        input("jh")
main()

    