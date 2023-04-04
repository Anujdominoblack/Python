#those objects that create a copy and  can not be changed are called immutable objects
name=True
another_name=name
print(id(name))
print(id(another_name))
name=False  #python can not change the original value so it creates a value false and assign it to result
print(id(name))
print(id(another_name))
print(another_name)  #the value of another is not changed as the values are not mutable
print(name)