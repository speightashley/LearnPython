shopping_list = ["computer",
                 "monitor",
                 "keyboard",
                 "mouse",
                 "mouse mat"
                 ]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))

a = b = c = d = e = f = another_list

b.append("cream")

print(b)
print(c)
