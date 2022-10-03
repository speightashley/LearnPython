panagram = "The quick brown fox jumps over the lazy dog"

words = panagram.split()
print(words)

numbers = "9,223,376,545,744,345"

generated_list = numbers.split(",")
print(generated_list)

# replace values in place

for index in range(len(generated_list)):
    generated_list[index] = int(generated_list[index])
print(generated_list)

# create a new list

integer_values = []

for value in generated_list:
    integer_values.append(int(value))

print(integer_values)
#  for number in numbers:
#  int(number).
