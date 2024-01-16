farm_animals = {"sheep","hen","cow","horse","goat"}
wild_animals = {"lion","elephant","tiger","goat","panther","horse"}

# now we will   create union using both union method and union operator

all_animals = farm_animals.union(wild_animals)  # union method returns a set

print(all_animals)

# now using union operator

check_animals = farm_animals | wild_animals
print(check_animals)