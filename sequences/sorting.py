pangram = "The quick brown fox jumps over the lazy dog"

letter = sorted(pangram)

print(letter)

numbers = [2.4, 5.6, 5.7, 7.8, 2.6, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog", key=str.casefold)

names = ["Graham",
         "jon",
         "Terry",
         "eric",
         "terry"
         ]

names.sort(key=str.casefold)

