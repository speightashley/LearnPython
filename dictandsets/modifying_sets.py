numbers = set()

print(numbers, type(numbers))

# print(numbers)

while len(numbers) < 4:
    next_value = int(input("Please enter your next value: "))
    numbers.add(next_value)
print(numbers)
