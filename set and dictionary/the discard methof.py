travel_mode ={"1":"car" , "2":"plane",}

items={"can opener","fuel","jumper","knife","matches","razor blades","razor","scissors","shampoo",
        "shaving_cream ","shirts","shorts","sleeping bag","soap","socks","stove","tent","mug",
       "tootbrush","toothpaste","towel","underwear","water carrier",}

restricted_items ={
    "catapault","fuel","gun","knife","razor blades","scissors","shampoo",}

for key,value in travel_mode.items():
    print(f"{key} {value}")

mode= input("enter the mode of transport")

if mode=="2":
    for item in restricted_items:

        items.discard(item)  # here we use discard cause if we use remove and restricted is not there error will throw

print(items)