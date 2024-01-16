farm_animals = {'cow','sheep','hen','goat','horse'}

print(farm_animals)

print()

wild_animals = {'sheep','goat','cow','horse','hen'}  # the two sets are equal order and sequence do not matter

print(wild_animals)
# so we can say python considers sets to be equal if they contain same item.ordering is not important
print()

if wild_animals == farm_animals:  # checking if two sets are equal condition is true
    print("the two sets are same")

else:
    print("the sets are different")