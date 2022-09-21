age = int(input("How old are you? "))

if 16 <= age <= 65:  # if age in range(16, 66):
    print("Have a good day at work")

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Enjoy work!")
    