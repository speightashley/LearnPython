a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# print()
# for i in range(1, 4):
#     print(i)
#
# i = 1
# print(i)
# i = 2
# print(i)
# i = 3
# print(i)

# Operator Precedence
print(a + b / 3 - 4 * 12)  # -35.0
print(a + (b / 3) - (4 * 12))  # -35.0
print(((a + b) / 3 - 4) * 12)  # 12
print(((a + b) / 3 - 4) * 12) # 12

c = a + b
d = c / 3
e = d - 4
print(e * 12)
