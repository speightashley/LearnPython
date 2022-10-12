def multiply(a, b):
    """
    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.
    
    :param a: I need an `int` to multiply.
    :param b: I need another `int` to multiply.
    :return: The product of the two numbers.
    """
    return a * b  # TODO just testng the todo feature


answer = multiply(2, 4)
print(answer)


def is_palindrome(string):
    #  backwards = string[::-1]
    #  return backwards == string
    return string[::-1].casefold() == string.casefold()


# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("{} is a palindrome".format(word))
# else:
#     print("{} is not a palindrome".format(word))
#
# print()

answer = multiply(18, 3)
print(answer)
