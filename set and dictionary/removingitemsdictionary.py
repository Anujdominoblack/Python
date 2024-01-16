watches = {"1" : "omega",
        "2" : "tissot",
        "3" : "rolex" ,
        "4" : "audemars piguet",
        "5" : "patek phillipe"
}

for key in watches:
    print(key,watches[key],sep=" ,")

# we will delete the elements in dictionary using key values

del watches['2']  # use del keyowrd and then provide the key element you want to delete

for key,value in watches.items():
    print(key,value,sep=" ,")