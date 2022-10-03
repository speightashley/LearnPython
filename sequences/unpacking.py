a = b = c = d = e = f = 12
print(c)

print("Unpacking a tuple")

data = 1, 2, 76  # it's a tuple
x, y, z = data
print(x)
print(y)
print(z)

print("Unpacking a list")
data_list = [12, 13, 14]
data_list.append(15) # causes error because we only expect 3 bits of data below

p, q, r = data_list
print(p)
print(q)
print(r)
