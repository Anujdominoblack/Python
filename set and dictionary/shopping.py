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


dict_display={}

for index,key in enumerate(recipes):
    dict_display[str(index+1)] = key

while True:
    print("choose your recipe")
    print("__________________")

    for key,value in dict_display.items():
        print(f"{key} {value}")

    choice =input("<")

    if choice == "0":
        break
    elif choice in dict_display:
        selected = dict_display[choice]
        print(f"the ingredietns are ")
        ingredient = recipes[selected]
        print(f"{ingredient}")

        for food_item,quantity in ingredient.items():
            available = pantry.get(food_item,0)
            if quantity<=available:
                print(f" food item {food_item} okay")
            else:
                tobuy=quantity-available
                print(f"to buy {food_item}",tobuy)

