"""
This cod is abt turl3jrfjufhsjffhff
"""

import turtle

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


def pattern(turta, hexa_color, square_color, circle_color, border_color):
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
        hexa_color = input("Enter the color of hexagon: ")
        circle_color = input("Enter the color of circle: ")
        square_color = input("Enter the color of square: ")
        border_color = input("Enter the color of shape borders: ")
        turta = turtle.Turtle()
        pattern(turta, hexa_color, square_color, circle_color, border_color)
        turtle.done()
main()