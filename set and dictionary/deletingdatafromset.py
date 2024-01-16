small_ints = set(range(21))
print(small_ints)

# use of discard method

small_ints.discard(10)
print(small_ints)

# use of remove method

small_ints.remove(12)
print(small_ints)

# difference between discard and remove

# when we use discard if the element is  not present in set it will throw an error

# when we use remove and if the element is not present it will throw an error

small_ints.discard(99)
print(small_ints)  # it will not throw an error

# now use  remove

small_ints.remove(99)
print(small_ints)  # error throwed 