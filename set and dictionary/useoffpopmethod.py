watches = {
       "1" : 'omega',
    "2": 'rolex',
    "3" : 'tissot',
    "4" : "ap"
}

for key in watches:
    print(key,watches[key])


watches.pop("3",None)  # if the key doesnt exist that we want to  delete do not exist it returns default value

for key in watches:
    print(key,watches[key])

result = watches.pop("6","this dont exist")

print(result)