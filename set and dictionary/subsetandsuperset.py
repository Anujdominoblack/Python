animals = {'turtle','horse','ruby','python','sparrow','hedgehog','wren','aarduark','cat',}

birds = {'robin','sparrow','wren'}

# note

# issubset() it returns either true or false and used to find subset
# issuperset() it returns either true or false and used to find superset

print(birds<=animals)
print(birds<animals) # proper subset

print(animals.issuperset(birds))

garden_birds = {'sparrow','robin','wren'}

print(birds.issuperset(garden_birds))
print(birds>garden_birds)
