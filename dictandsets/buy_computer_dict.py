available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "hdmi cable",
    "6": "DVD Drive",
}

current_choice = None
computer_parts = {}  # create an empty dictionary

while current_choice != 0:
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            #it's already in so remove it
            print(f"removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"Your dictionary now contains {computer_parts}")
    else:
        for key, value in available_parts.items():
            print(f"{key}: {value}")
    current_choice = input("> ")

