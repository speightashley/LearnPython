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

        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # if it's already in, so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options form the list below")
        for number, part in enumerate(available_parts):
            print("{}: {}".format(number + 1, part))
    current_choice = input()

print(computer_parts)
