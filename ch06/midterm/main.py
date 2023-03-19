import turtle

def direction1(x,y):
    pen.forward(x)
    pen.right(y)

def direction2(x,y):
    pen.forward(x)
    pen.left(y)

def curve(x,y,z):
    for i in range(x):
        pen.right(y)
        pen.forward(z)

pen = turtle.Turtle()
paper = turtle.Screen()

def main():
    angle = 90
    pen.left(angle)
    pen.up()
    pen.forward(200)
    pen.down()
    pen.right(angle)
    direction1(60,70)
    direction2(75,15)
    direction1(30,5)
    direction2(50,20)
    pen.forward(40)
    curve(4,10,20)
    direction1(30,10)
    direction1(50,30)
    direction1(100,90)
    direction1(10,60)
    direction2(40,130)
    direction1(50,5)
   


main()

paper.exitonclick()