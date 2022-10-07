def multiply(a, b):
    return a * b  # TODO just testng the todo feature


answer = multiply(2, 4)
print(answer)


def is_palindrome(string):
    #  backwards = string[::-1]
    #  return backwards == string
    return string[::-1].casefold() == string.casefold()


word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("{} is a palindrome".format(word))
else:
    print("{} is not a palindrome".format(word))

print()
