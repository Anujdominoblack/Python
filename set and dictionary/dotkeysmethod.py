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

# dot keys method returns the list of all the keys present in the dictionary the syntax is

# dictionaryname.keys()

# for example

key = d.keys()

print(key)  # the output is a view object

d[10] = "ten"

print(key)
  # if we update dictionary key is also updated
for item in d:  #  this method also print all the keys present in the dictionary
    print(item)

# a more efficient approach of knowing is that we know exactly we are traversing through keys example

for item in (d.keys()):
    print(item)