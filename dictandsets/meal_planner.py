from contents import pantry, recipes


#  display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}

def add_shopping_item(data: dict, items: str, amount: int) -> None:
    """Add a tuple containing item and amount to the data dict"""
    #    if items in data:
    #       data[item] += amount
    #  else:
    #     data[item] = amount
    data[items] = data.setdefault(item, 0) + amount


display_dict = {}

for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_list = {}

while True:
    #  Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("Checking ingredients...")
        ingredients = recipes[selected_item]
        for item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {item}")
                add_shopping_item(shopping_list, item, quantity_to_buy)

for things in shopping_list:
    print(things)
