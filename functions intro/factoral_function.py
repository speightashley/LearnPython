def factorial(number):
    """
    Returns the facotiral number
    :param number:
    :return:
    """
    if number <= 1:
        return 1
    answer = 2
    for x in range(3, number + 1):
        answer *= x

    return answer


for i in range(36):
    print(i, factorial(i))
