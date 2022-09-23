import random
highest_option = 10
answer = random.randint(1, highest_option)
guess = None

while guess != answer:
    guess = int(input("what is your guess? "))
    if guess > answer:
        print("Guess lower")
    elif guess < answer:
        print("Guess higher")
    else:
        print("You got it right!")
        break
