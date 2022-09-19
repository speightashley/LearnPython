for i in range(1, 13):
    print("no. {} squared is {:3} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("*" * 80)

name = input("Please enter you name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote")
    print("Please put an x in the box")
else:
    print("Please come back in {} years".format(18 - age))

