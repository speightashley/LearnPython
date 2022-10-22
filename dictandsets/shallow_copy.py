import copy

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

things = animals.copy() # shallow copy - Copies the dict but only with pointers to the existing contents

things2 = copy.deepcopy(animals)  # Deep Copy - Actually copies the dict and creates a new space in memory for it

print(things["teddy"])
print(animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
