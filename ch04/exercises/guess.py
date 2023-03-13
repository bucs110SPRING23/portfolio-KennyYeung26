import random
randomInteger = random.randrange(1,1001)

count = 0

while (True):
    guess = int(input("Guess the number:"))
    count = count + 1
    if guess == randomInteger:
        print("correct!")
        break
    elif guess > randomInteger:
        print("too high!")
    elif guess < randomInteger:
        print("too low!")

print("the correct answer is", randomInteger)
print("The number of guesses is", count)