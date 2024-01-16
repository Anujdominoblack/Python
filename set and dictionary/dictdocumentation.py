d = {
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
}

pantry_items =['chicken','spam','egg','bread','lemon']

# now we will use fromkey method from dict class it takes iterable and create dictionary associated with it

new_dict = dict.fromkeys(pantry_items)

# we will pass a iterable to from keys which takes iterable elements as  keys and assigns
# value to them and returns a dictionary

# we can also define default values to the keys  for example

second_dict = dict.fromkeys(pantry_items,0)

# not that we can define strings as a value for the key also

# for example

third_dict = dict.fromkeys(pantry_items,"syystumm")

print(new_dict)

print(second_dict)

print(third_dict)