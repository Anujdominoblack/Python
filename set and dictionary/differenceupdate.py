travel_mode ={"1":"car" , "2":"plane",}

items={"can opener","fuel","jumper","knife","matches","razor blades","razor","scissors","shampoo",
        "shaving_cream ","shirts","shorts","sleeping bag","soap","socks","stove","tent","mug",
       "tootbrush","toothpaste","towel","underwear","water carrier",}

restricted_items ={
    "catapault","fuel","gun","knife","razor blades","scissors","shampoo",}

mode =input("enter your choice")

if mode == '2':
    items -= restricted_items   # set difference update method

print("you need to pack")

for items in sorted(items):
    print(items)