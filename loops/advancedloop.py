number = "9,233;372:036 854,755;807"
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])

quote = """Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, Irrigation, Roads, the Fresh-Water System, and Public Health, what have the Romans ever done for us?
"""
capitals = ""
for char in quote:
    if char.isupper():
        capitals = capitals + char

print(capitals)
