# t = "a", "b", "c"
# print(t)

welcome = "welcome to my nightware", "Alice Cooper", 1975
bad = "Bad company", "Bad company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the lightning", "metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])

name, length, width, height, price = table

print(length * width)

metallica2 = list(metallica)

print(metallica2)
metallica2[0] = "Master of Puppets"

print(metallica2)