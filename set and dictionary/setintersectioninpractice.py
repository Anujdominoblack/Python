trial1={"bob","charley","georgia","john",}

trial2={"anne","charley","eddie","georgia"}

checkset = trial1.intersection(trial2)
print(checkset)

farm_animals = {"sheep","goat","hen","cow","horse",}

wild_animals = {"lion","tiger","panther","elephant","horse"}

powerful_animals = {"horse","lion","tiger",}

# using operand method of intersection

print(farm_animals & wild_animals & powerful_animals)  # operand method

# we can pass one or more set or data items to intersection method
animals = farm_animals.intersection(wild_animals,powerful_animals)

print(animals)