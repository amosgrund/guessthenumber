#guess the number game you cant win 2

#import

import random

#question

print("Guess a number from 1 to 10:\n")

#loop

while True:

    guess = int(input())

    number = random.randint(1, 10)

    while guess==number:
        number = random.randint(1, 10)

    if guess > 0 and guess < 11:
        print("That's not the number we're looking for. We are looking for",  str(number) + ". Try again:\n")
    else:
        print("That's not a number from 1 to 10. Try another number:\n")