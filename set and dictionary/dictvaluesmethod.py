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

pantry_items = ['chicken','spam','egg','bread','lemon']

v= d.values()  # it returns the value of a dictionary  and the syntax is dictionaryname.values()

print(v)  # it returns the view object of the all the values

# now of we change the value in dictionary it will also be changes

d[10]="ten"

print(v)

# now we can use values method to check if values exist in dictionary

print("four" in v)

print("somethinf " in  v)

# converting key and values in list type

keys = list(d.keys())
values = list(d.values())
 # the view type is converted into the list type
print(keys)
print(values)

if "four" in values:
    index = values.index("four")
    keys=keys[index]
    print(f"{d[keys]}  {keys}")


# same can be done using loop

for key,value in d.items():
    if value == "four":
        print(f"{d[key]} , {key}")