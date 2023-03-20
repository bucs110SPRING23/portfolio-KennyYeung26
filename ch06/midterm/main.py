import turtle
import math

pen1 = turtle.Turtle()
pen1.speed(30)
pen1.width(3)
pen2 = turtle.Turtle()
pen2.speed(30)
pen2.width(3)
paper = turtle.Screen()

def direction1(x,y):
    '''
    This function allows both pen1 and pen2 to move forward and right together.
    args: x (int) magnitude of movement, y (int) magnitude of angle
    return: None
    '''
    pen1.forward(x)
    pen1.right(y)
    pen2.forward(x)
    pen2.right(-1 * y)

def direction2(x,y):
    '''
    This function allows both pen1 and pen2 to move forward and left together.
    args: x (int) magnitude of movement, y (int) magnitude of angle
    return: None
    '''
    pen1.forward(x)
    pen1.left(y)
    pen2.forward(x)
    pen2.left(-1 * y)

def curve(x,y,z):
    '''
    This function allows both pen1 and pen2 to move at a certain distance and angle that loops, allowing a curve to be formed.
    args: x (int) magnitude of loop, y (int) magnitude of angle, z (int) magnitude of movement
    return: None
    '''
    for i in range(x):
        pen1.right(y)
        pen1.forward(z)
        pen2.left(y)
        pen2.backward(-1 * z)

def reposition(x,y):
    '''
    This function allows both pen1 and pen2 to move to another position on the drawing without leaving lines.
    args: x (float) x-coordinate, y (float) y-coordinate
    return: None
    '''
    pen1.up()
    pen1.goto(x,y)
    pen1.down()
    pen2.up()
    pen2.goto(-1 * x,y)
    pen2.down()

def head():
    pen1.left(90)   #head outer outline
    pen1.up()
    pen1.forward(200)
    pen1.down()
    pen1.right(90)
    pen2.left(90)
    pen2.up()
    pen2.forward(200)
    pen2.down()
    pen2.left(90)
    direction1(60,70)
    direction2(75,15)
    direction1(30,5)
    direction2(50,20)
    pen1.forward(40)
    pen2.forward(40)
    curve(4,10,20)
    direction1(30,10)
    direction1(50,30)
    direction1(100,90)
    direction1(10,60)
    direction2(40,130)
    direction1(70,90)
    direction2(20,100)
    pen1.color("red")   #mouth
    pen2.color("red")
    direction1(30,30)
    direction1(56,110)
    pen1.up()
    pen2.up()
    direction1(25,60)
    pen1.down()
    pen2.down()
    pen1.forward(50)
    pen2.forward(50)
    direction2(-30,75)
    pen1.color("black")
    pen2.color("black")
    direction2(25,18)
    pen1.forward(20)
    pen2.forward(20)
    direction1(-20,18)
    direction1(-25,75)
    pen1.color("red")
    pen2.color("red")
    direction2(30,40)
    direction1(10,45)
    direction1(20,98)
    pen1.color("black")
    pen1.forward(26)
    pen1.backward(26)
    pen1.left(150)
    pen2.color("black")
    pen2.forward(26)
    pen2.backward(26)
    pen2.right(150)
    direction1(50,30)
    direction2(60,45)
    direction2(30,110)
    direction2(100,45)
    pen1.color("red")
    pen2.color("red")
    direction1(25,45)
    pen1.forward(15)
    pen1.color("black")
    pen2.forward(15)
    pen2.color("black")
    reposition(13.32,-98.19)
    pen1.left(120)
    pen2.right(120)
    direction2(20,50)
    direction1(15,40)
    direction2(15,50)
    pen1.forward(28)
    pen2.forward(28)
    reposition(49.27,-167.49)
    pen1.left(60)
    pen2.right(60)
    direction1(30,52)
    pen1.forward(23)
    pen2.forward(23)
    reposition(29.57,-72.56)    #eyes
    pen1.right(120)
    pen1.color("green")
    pen2.left(120)
    pen2.color("green")
    direction2(20,60)
    direction2(15,62)
    direction2(65,70)
    pen1.forward(19)
    pen2.forward(19)
    reposition(116.85,-67.70)   #cheeks
    pen1.right(160)
    pen1.color("black")
    pen2.left(160)
    pen2.color("black")
    direction1(15,32)
    pen1.forward(85)
    pen2.forward(85)
    reposition(23.08,-75.18)    #center red piece
    pen1.right(200)
    pen2.left(200)
    pen1.color("red")
    pen2.color("red")
    direction2(45,40)
    direction2(60,50)
    direction1(18,0)
    reposition(17.95,23.49)   #shape above red piece
    pen1.right(85)
    pen2.left(85)
    pen1.color("black")
    pen2.color("black")
    direction2(100,40)
    direction2(40,62)
    direction2(30,0)
    reposition(26.93,156.3)
    pen1.right(125)
    pen2.left(125)
    direction2(54,0)
    reposition(23.08,-75.18)    #horns/antennas
    pen1.right(30)
    pen2.left(30)
    direction2(142,45)
    direction1(55,45)
    direction2(180,175)
    direction1(290,25)
    direction2(15,20)
    direction2(28,0)
    reposition(65.80,11.28)
    pen1.left(60)
    pen2.right(60)
    direction1(33,45)
    direction1(20,0)
    reposition(80,60)   #circles
    pen1.circle(20)
    pen2.circle(-20)
    reposition(-0.59,-103.81)   #give dimension to center red piece
    pen1.right(117)
    pen2.left(117)
    pen1.color("red")
    pen2.color("red")
    direction1(30,40)
    direction1(60,0)

def sunrays(radians):
    '''
    This function allows user to calculate coordinates.
    args: radians (float) input radians to get coordinate values
    return: coordinates (float) coordinate points that act as the starting point for the sunrays lines to be drawn
    '''
    coordinates = []
    coordinates.append(300 * math.cos(radians))
    coordinates.append(300 * math.sin(radians))
    return coordinates

def sun():
    '''
    This function allows lines to be drawn extruding outwards in a circle.
    args: None
    return: None
    '''
    for i in range(0,16):
        coordinates = sunrays(math.pi/8 * i)
        reposition(coordinates[0],coordinates[1])
        pen1.forward(60)
        pen1.left(22.5)

def main():
    head()
    sun()

main()

paper.exitonclick()