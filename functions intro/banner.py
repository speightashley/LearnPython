def banner_text(text=" ", screen_width=80):
    """

    :param text:
    :param screen_width:
    :return:
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}".format(text, screen_width))
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)
