for i in range(1, 13):
    print("no. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# {0:2}  is a format specification. It states that we show the numbers with that amount of space
print()

for i in range(1, 13):
    print("no. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
    # <3 / <4 left aligns the numbers

for i in range(1, 13):
    print("no. {0:2} squared is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
    # ^3 / ^4 centres of the writing

print()

print("pi is approx {0:12}".format(22 / 7))
print("pi is approx {0:12f}".format(22 / 7))
print("pi is approx {0:12.50f}".format(22 / 7))
print("pi is approx {0:52.50f}".format(22 / 7))
print("pi is approx {0:62.50f}".format(22 / 7))

