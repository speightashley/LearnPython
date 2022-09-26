available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "HDMI Cable"
                   ]
current_choice = "-"
computer_parts = []  # create and empty list

valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]

while current_choice != '0':
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
    else:
        print("Please add options form the list below")
        for number, part in enumerate(available_parts):
            print("{}: {}".format(number + 1, part))
    current_choice = input()

print(computer_parts)
