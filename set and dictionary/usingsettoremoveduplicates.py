data = ["blue","red","blue","green","red","blue","white"]

# creating a set from list removing duplicates

unique_data = set(data)
print(unique_data)   # it prints and creates a set with all distinct items

# creating a sorted list

unique_data =sorted(set(data))  # the sorted function will take any iterable and produce a list
print(unique_data)

# if we want to preserve ordering create a dictionary
# create a list of unique colours keeping order

unique_data = dict.fromkeys(data)
print(unique_data)

unique_data =list(dict.fromkeys(data)) # when we  convert dictionary to list keys are used as element
print(unique_data)