#Part 1:
def multiplication(x,y):
    number = 0
    for i in range(x):
        number = number + y
    return number

print(multiplication(2,3))
            
#Part 2:
def exponents(x,y):
    number = 1
    for i in range(y):
        number = number * x
    return number

print(exponents(2,3))

#Part 3:
def square(x):
    return multiplication(x, x)

print(square(2))