# implications of sets being unordered

farm_animals ={'cow','sheep','hen','goat','horse'}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print()

print("indexing a sequence")

animals_list =['cow','sheep','hen','goat ','horse']
print(animals_list)

print(animals_list[4])  # indexing a list

# trying to index a set

print()

print(farm_animals[2])  # it will throw an error as object is not subscriptable that means
                        # we can't index a set

print()

