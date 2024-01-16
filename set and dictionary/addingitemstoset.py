numbers={}  # it will create a empty dictionary not set
print(type(numbers))

# creating empty set

numbers1 = set()

print(type(numbers1))

# adding a items to set

numbers1.add(1)
print(numbers1)

while len(numbers1)<5:
    next_value=int(input("enter the number you want to add in the set"))
    numbers1.add(next_value)

print(numbers1)