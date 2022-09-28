data = [4, 5, 104, 105, 110, 120, 130, 150, 170]


print(data)
del data[14:]
print(data)

min_value = 100
max_value = 200

# for index, value in enumerate(data):
#     if (value < min_value) or (value > max_value):
#         del data[index]
#
# print(data)

stop = 0
for index, value in enumerate(data):
    if value >= min_value:
        stop = index
        break

del data[:stop]
print(data)
