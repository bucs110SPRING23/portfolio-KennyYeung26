#Part A:

import turtle

window = turtle.Screen()
Turtle1 = turtle.Turtle()
Turtle2 = turtle.Turtle()
Turtle1.pos()
Turtle1.penup()
Turtle1.goto(-100,20)
Turtle1.pendown()

Turtle2.pos()
Turtle2.penup()
Turtle2.goto(-100,-20)
Turtle2.pendown()

#Race 1:
import random

random1 = random.randrange(1,101)
Turtle1.forward(random1)
random2 = random.randrange(1,101)
Turtle2.forward(random2)

Turtle1.goto(-100,20)
Turtle2.goto(-100,-20)


#Race 2:
for i in range(1,11):
    Turtle1.forward(random.randrange(1,11))
    Turtle2.forward(random.randrange(1,11))
Turtle1.goto(-100,20)
Turtle2.goto(-100,-20)

window.exitonclick()

#Part B
import pygame
import math

pygame.init()
window = pygame.display.set_mode()