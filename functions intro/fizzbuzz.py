def fizz_buzz(number: int) -> str:
    """
    Returns the next number in line from the number provided. With numbers divisible
    by 3 and 5 returning `fizz buzz` and numbers divisible by 3 returning `fizz`
    :param number: Number provided by the user
    :return: String of fizz, buzz or fizz buzz or number
    """
    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


for i in range(1, 101):
    print(fizz_buzz(i))

