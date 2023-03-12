import pygame

#Part A:

def threenp1(n):
    while not n == 1:
        count = 0
        while n > 1.0:
            if n % 2 == 0:
                n = int(n / 2)
            else:
                n = int(3 * n + 1)
            count = count + 1
        return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for i in range(2, upper_limit + 1):
        count = threenp1(i)
        objs_in_sequence[i] = count
    return objs_in_sequence

def main():
    print(threenp1range(10))

main()
        
