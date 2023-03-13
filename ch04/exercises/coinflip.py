import turtle
import random

turtle1 = turtle.Turtle()
window = turtle.Screen()

distance = 20
angle = 90
is_in_screen = True

while is_in_screen:
    coin = random.randrange(0, 2)
    if coin:
        turtle1.right(angle)
    else:
        turtle1.left(angle)
    turtle1.forward(distance)

def is_in_screen(window, turtle1):
    left_bound = window.window_width() / 2
    right_bound = window.window_width() / 2
    top_bound = window.window_width() / 2
    bottom_bound = window.window_width() / 2

    turtleX = turtle1.xcor()
    turtleY = turtle1.ycor()

    x_range = window.window_width() / 2
    y_range = window.window_width() / 2
    still_in = True


window.exitonclick()
