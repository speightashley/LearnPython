albums = [("welcome to my nightware", "Alice Cooper", 1975),
          ("Bad company", "Bad company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the lightning", "metallica", 1984)
          ]

print(len(albums))

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))
