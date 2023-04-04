shopping=['milk','rice','tea','coffee','sugar']
another=shopping
print((id(shopping)))
print(id(shopping))
shopping +="pasta"
print(shopping)
print(id(shopping))  #here the id will not be changed as list are mutable and can be reconfigured
print(id(another))