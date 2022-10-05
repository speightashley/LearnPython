def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    if string == string[::-1]:
        print("it's a palindrome")
    else:
        print("It's not a palindrome")


palindrome_sentence("was it a car or a cat i saw")


