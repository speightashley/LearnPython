import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {} ".format(highest))
guess = int(input())

if guess == answer:
    print("You got it right first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:  # guess must be greater than answer
        print("Please guess lower")
        guess = int(input())
        if guess == answer:
            print("Well done innit")
        else:
            print("Sorry, you haven't guessed correctly")


# if guess < answer:
#     print("Please guess higher")
# elif guess > answer:
#     print("Please guess lower")
# else:
#     print("You got it right!")

