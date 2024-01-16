# we will add values in dictionary using the keys

car = {
    '1':'ferrari',
    '2' : 'lambo',
    '3':'aston martin',
    '4':'buggati'
}

for key in car:
    print(key,car[key] ,sep=" ,")


# now we will add items in dict

car['5'] = 'pagani'

for key in car:
    print(key,car[key],sep=' ,')