import random

user = int(input("Please enter a number between 1 to 9 to play this game:"))

y = random.randrange(10)

if y == user:
    print("Congratulation you win")

else:
    print("better luck next time")