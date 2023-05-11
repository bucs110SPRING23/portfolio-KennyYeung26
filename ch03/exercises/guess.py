import random
random = random.randrange(1,11)

for guess in range(3):
    guess = int(input("Guess the number:"))
    if guess == random:
        print("correct!")
        break
    elif guess > random:
        print("too high!")
    elif guess < random:
        print("too low!")

print("the correct answer is", random)
