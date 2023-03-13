import turtle
sides = int(input("Enter the number of sides"))
length = int(input("Enter the length of each side"))
my_turtle = turtle.Turtle()
my_turtle.color('red')
window = turtle.Screen()
for i in range(sides):
    my_turtle.forward(length)
    my_turtle.left(360/sides)
print("Done")  
window.exitonclick()