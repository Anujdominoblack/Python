number="9.223,456,12231;45.2,67"
seperators=""
for char in number:
    if char .isnumeric():  #checks if char is numeric is not
        seperators=seperators+char
print(seperators)  #output

item=""
for char in number:
    if not char .isnumeric():  #checks if char is numeric is not
        item=item+char
print(item)  #output