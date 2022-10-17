def sum_numbers(*args: float) -> float:
    """
    Returns the sum of a collection of numbers
    :param args:
    :return:
    """
    return sum(args)


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
