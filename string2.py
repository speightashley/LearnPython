parrot = "Norwegian Blue"

print(parrot)
print(parrot[3])

print()
print(parrot[-1])

### Slicing
print(parrot[0:6])  # Norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])

# Print Blue challenge
print(parrot[10:])

print(parrot[:])

# Negative slices

print(parrot[-4:-2])
print(parrot[-4:12])

# Using steps with slices

print(parrot[0:6:2])  # NRE
print(parrot[0:6:3])

# slicing backwards

letters = "abcdefghijklmnopqrstvwxyz"

backwards = letters[25:0:-1]

print(backwards)
