#Part A

def star_pyramid():
    rows = int(input("Number of Rows: "))
    for i in range(1, rows + 1):
        print("*" * i)
star_pyramid()

#Part B

def rstar_pyramid():
    rows = int(input("Number of Rows: "))
    for i in range(rows, 0, -1):
        print("*" * i)
rstar_pyramid()