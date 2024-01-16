# when we do shallow copy the list elemnets is not copied only the refrences are copied into new dictionary
# and as copied contains only refrences  to lists changes in one reflect in other

lion_list =["scary","big","cat"]
elephant_list=["big","grey","wrinkled"]
teddy_list=["cuddly","softy"]

animals ={
    "lion" : lion_list,
    "elephant" : elephant_list,
    "teddy" :teddy_list,
}

things = animals.copy()  # here it crreates only a shallow copy and only refrences are copied both pointing to same
                         # dictionary and hence changes reflect in each other


print(things["teddy"])
print(animals["teddy"])

things["teddy"].append("toy")   # now both refer to same chnages in value  which is list that why append work
                                # appeared on other copied dictionary
print(things["teddy"])
print(animals["teddy"])

animals["teddy"].append("this is added by animals")
things["teddy"].append("it is added by plants ")

print(things["teddy"])
print(animals["teddy"])


#  a shallow copy only copies refrences 