import turtle

dex = turtle.Turtle()
screen = turtle.Screen()


# functions for turtle
def moveW():
    dex.forward(5)


def moveD():
    dex.right(5)


def moveS():
    dex.back(5)


def moveA():
    dex.left(5)


def clearscreen():
    dex.home()
    dex.clear()


screen.listen()
screen.onkey(moveW, 'w')
screen.onkey(moveA, 'a')
screen.onkey(moveS, 's')
screen.onkey(moveD, 'd')
screen.onkey(clearscreen, 'c')

screen.exitonclick()
