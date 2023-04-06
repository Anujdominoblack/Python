empty_list=[]
even=[2,4,6,8]
odd=[1,3,5,9]
numbers=[even,odd]
print(numbers)
for item in numbers:  #we need two loops for traversal and printing purposes
    print(item)
    for values in item:
        print(values)