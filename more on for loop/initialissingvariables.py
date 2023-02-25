shopping_list=["milk","rice","water","spice","yogurt","curd","mango"]
itemtofind="milk"
found=None
for index in range(len(shopping_list)):  #len returns the length of the list
    if shopping_list[index]==itemtofind:
        found=index
        break;
print("item is found at positon {}".format(found))
