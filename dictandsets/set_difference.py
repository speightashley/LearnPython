from primesandsquares import squares_generator, primes_generator

evens = set(range(0,50,2))
odds = set(range(1, 51, 2))

print(odds)
print(evens)

primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)

print(odds.difference(primes))
