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

# now we will do enumerate method that will do tuple unpacking and key value is created and using that dict is updated

d.update(enumerate(pantry_items))

for key,value in d.items():
    print(key,value)