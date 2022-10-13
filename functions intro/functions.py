def multiply(a: float, b: float) -> float:
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


def is_palindrome(string: str) -> bool:
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

def fibonacci(n: int) -> int:
    """
    Return the `n` th fibonacci number, for positive `n` .
    :param n:
    :return:
    """
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0
    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    return result


for i in range(36):
    print(i, fibonacci(i))

