# dot update mehtod is used to update the contents of dictionary by using another dictionary

# if the both the dictionary contains the same element then the values in the first dictionary will be updated

# or if key is unique then in the resultant dictionary the new key is inserted

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

d1={
    1:"this is one",
    7:"this is seven",
    10:"ten",
}

# now we will update dictionary 1 using 2

d.update(d1)  # we are updating dictioanry d with the contents of d1

for item,value in d.items():  # .items() returns iterator of tuples and tuple unpacking is done
    print(item ,value)     # we can see in the output that key is updated or added