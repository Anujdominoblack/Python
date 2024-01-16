animals = {
     "lion" :"scary",
     "elephant" : "big",
     "teddy" : "cuddly" ,

}

things = animals.copy()  # it copies the dictionary and create another dictionary

animals["teddy"] = "toy" # changing key value
print(animals["teddy"])
print(things["teddy"])  # in this change in one is not reflecting in other

