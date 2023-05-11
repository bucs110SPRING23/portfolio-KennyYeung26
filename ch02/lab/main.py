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
window.fill("white")
pygame.time.wait(1000)

#triangle
points = []
num_sides = 3
side_length = 200
xpos = 750
ypos = 400

for i in range(num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    points.append([x,y])
pygame.draw.polygon(window, "red", points)
pygame.display.flip()
pygame.time.wait(1000)

window.fill("white")
pygame.display.flip()

#square
points = []
num_sides = 4
side_length = 200
xpos = 750
ypos = 400

for i in range(num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    points.append([x,y])
pygame.draw.polygon(window, "blue", points)
pygame.display.flip()
pygame.time.wait(1000)

window.fill("white")
pygame.display.flip()

#hexagon
points = []
num_sides = 6
side_length = 200
xpos = 750
ypos = 400

for i in range(num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    points.append([x,y])
pygame.draw.polygon(window, "yellow", points)
pygame.display.flip()
pygame.time.wait(1000)

window.fill("white")
pygame.display.flip()

#icosagon
points = []
num_sides = 20
side_length = 200
xpos = 750
ypos = 400

for i in range(num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    points.append([x,y])
pygame.draw.polygon(window, "green", points)
pygame.display.flip()
pygame.time.wait(1000)

window.fill("white")
pygame.display.flip()

#hectagon
points = []
num_sides = 100
side_length = 200
xpos = 750
ypos = 400

for i in range(num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    points.append([x,y])
pygame.draw.polygon(window, "indigo", points)
pygame.display.flip()
pygame.time.wait(1000)

window.fill("white")
pygame.display.flip()

#circle
points = []
num_sides = 360
side_length = 200
xpos = 750
ypos = 400

for i in range(num_sides):
    angle = 360/num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    points.append([x,y])
pygame.draw.polygon(window, "violet", points)
pygame.display.flip()
pygame.time.wait(1000)