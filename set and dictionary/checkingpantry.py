pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes = {
    "Butter chicken": {
        "chicken": 750,
        "lemon": 1,
        "cumin": 1,
        "paprika": 1,
        "chilli powder": 2,
        "yogurt": 250,
        "oil": 50,
        "onion": 1,
        "garlic": 2,
        "ginger": 3,
        "tomato puree": 240,
        "almonds": 25,
        "rice": 360,
        "coriander": 1,
        "lime": 1,
    },
    "Chicken and chips": {
        "chicken": 100,
        "potatoes": 3,
        "salt": 1,
        "malt vinegar": 5,
    },
    "Pizza": {
        "pizza": 1,
    },
    "Egg sandwich": {
        "egg": 2,
        "bread": 80,
        "butter": 10,
    },
    "Beans on toast": {
        "beans": 1,
        "bread": 40,
    },
    "Spam a la tin": {
        "spam": 1,
        "tin opener": 1,
        "spoon": 1,
    },
}


display_dict ={}

for index,key in enumerate(recipes):
    display_dict[str(index+1)] = key

while True:
    print("please enter your choice ")
    print("_________________________")
    for key,value in display_dict.items():
        print(f"{key} {value}")

    choice = input("<<")

    if choice =="0":
        break

    elif choice in display_dict:
        print("your selected item is")
        selected = display_dict[choice]
        print("your selected ingredients are ")
        ingredients = recipes[selected]

        print(ingredients)

        # now we will check pantry

        for food_item ,required in ingredients.items():
            quantity_in = pantry.get(food_item,0)
            if required<=quantity_in:
                print("item is in pantry")

            else:
                quantity_buy=required-quantity_in
                print(f"{quantity_buy}")

