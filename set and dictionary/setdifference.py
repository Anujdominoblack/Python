# set difference is the set of all items that is present in one set but not in another

from primes import squares_generator,primes_generator

even =set(range(0,50,2))

odd = set(range(1,50,2))

print(even)
print(odd)

prime = set(primes_generator(100))

square = set(squares_generator(100))

print(prime)
print(square)

# using difference method

print(odd.difference(prime))  # it returns a new set

# using operand of set difference

print(odd - prime)

# using difference update method
# which modifies the original set

print(even.difference_update(square))


