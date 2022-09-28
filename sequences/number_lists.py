even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
empty_list = []

numbers = even + odd
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)


print(min(even))
print(max(even))
print(min(odd))
print(max(odd))

print()
print(len(even))
print(len(odd))

print()
print("mississippi".count("iss"))

even.extend(odd)
print(id(even))
print(even)
another_even = even
print(another_even)
even.sort(reverse=True)
print(id(even))
print(even)
