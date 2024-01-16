animals = {
     "lion" :"scary",
     "elephant" : "big",
     "teddy" : "cuddly" ,

}

things = animals
# both things and animals refer to the same dictionary so changing one will reflect in other 
animals["teddy"] = "toy"
print(things["teddy"])