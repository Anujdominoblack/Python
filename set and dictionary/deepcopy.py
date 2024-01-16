#deep copy
# in deep copy we will create copies of lists ,dictionaries and other mutable objects
import copy # module needed for deep copy
animals = {
     "lion" : ["scary","big","cat"],
     "elephant" : ["big","gray","wrinkled"],
     "teddy" : ["cuddly","stuffed"] ,
}

# syntax for hard copy is copy.deepcopy(dictionaryname)

things = copy.deepcopy(animals)
print(things["teddy"])
print(animals["teddy"])
print()
things["teddy"].append("toy")

print(things["teddy"])
print(animals["teddy"])

# deep copy copies anyobjets
# shallow only copies refrences

pyhton = """ for i in range(10:
print(i) """
print(pyhton)