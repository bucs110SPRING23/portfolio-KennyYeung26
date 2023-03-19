import turtle

def direction1(x,y):
    for i in range(1):
        if y > 0:
            pen1.forward(x)
            pen1.right(y)
        elif y < 0:
            pen2.forward(x)
            pen2.right(y)
            

def direction2(x,y):
    for i in range(1):
        if y > 0:
            pen1.forward(x)
            pen1.left(y)
        elif y < 0:
            pen2.forward(x)
            pen2.left(y)

def curve(x,y,z):
    for i in range(x):
        if z > 0:
            pen1.right(y)
            pen1.forward(z)
        elif z < 0:
            pen2.left(y)
            pen2.backward(z)

pen1 = turtle.Turtle()
pen1.speed(20)
pen2 = turtle.Turtle()
pen2.speed(20)
paper = turtle.Screen()

def right_side():
    angle = 90
    pen1.left(angle)
    pen1.up()
    pen1.forward(200)
    pen1.down()
    pen1.right(angle)
    direction1(60,70)
    direction2(75,15)
    direction1(30,5)
    direction2(50,20)
    pen1.forward(40)
    curve(4,10,20)
    direction1(30,10)
    direction1(50,30)
    direction1(100,90)
    direction1(10,60)
    direction2(40,130)
    direction1(70,90)
    direction2(20,100)
    pen1.color("red")
    direction1(30,30)
    direction1(56,110)
    pen1.up()
    direction1(25,60)
    pen1.down()
    pen1.forward(50)
    direction2(-30,75)
    pen1.color("black")
    direction2(25,18)
    pen1.forward(20)
    direction1(-20,18)
    direction1(-25,75)
    pen1.color("red")
    direction2(30,40)
    direction1(10,45)
    direction1(20,98)
    pen1.color("black")
    pen1.forward(26)
    pen1.backward(26)
    pen1.left(150)
    direction1(50,30)
    direction2(60,45)
    direction2(30,110)
    direction2(100,45)
    pen1.color("red")
    direction1(25,45)
    pen1.forward(21)
    print(pen1.position())

def left_side():
    angle = 90
    pen2.left(angle)
    pen2.up()
    pen2.forward(200)
    pen2.down()
    pen2.left(angle)
    direction1(60,-70)
    direction2(75,-15)
    direction1(30,-5)
    direction2(50,-20)
    pen2.forward(40)
    curve(4,10,-20)
    direction1(30,-10)
    direction1(50,-30)
    direction1(100,-90)
    direction1(10,-60)
    direction2(40,-130)
    direction1(70,-90)
    direction2(20,-100)
    pen2.color("Red")
    direction1(30,-30)
    direction1(56,-110)
    pen2.up()
    direction1(25,-60)
    pen2.down()
    pen2.forward(50)
    direction2(-30,-75)
    pen2.color("black")
    direction2(25,-18)
    pen2.forward(20)
    direction1(-20,-18)
    direction1(-25,-75)
    pen2.color("red")
    direction2(30,-40)
    direction1(10,-45)
    direction1(20,-98)
    pen2.color("black")
    pen2.forward(26)
    pen2.backward(26)
    pen2.right(150)
    direction1(50,-30)
    direction2(60,-45)
    direction2(30,-110)
    direction2(100,-45)
    pen2.color("red")
    direction1(25,-45)
    pen2.forward(21)

def main():
    right_side()
    left_side()

main()

paper.exitonclick()