available_parts = {
    "1" : "computer",
    "2" : "monitor",
    "3" : "keyboard",
    "4" : "mouse",
    "5" : "hdmi cable",
    "6" : "dvd drive"
}

current_choice =None
# creting an empty dict for storing available parts

computer_part={}
while current_choice !="0":
    if current_choice in available_parts:
        chosen_part=available_parts[current_choice]
        if current_choice in computer_part:
            print(f"remove {chosen_part}")
            computer_part.pop(current_choice)

        else:
            print(f"adding {chosen_part}")
            computer_part[current_choice]=chosen_part

            print(f"dictionary contains {computer_part}")



    else:
        print("choose items from below list")
        for key in available_parts:
            print(key,available_parts[key],sep=" ,")
    current_choice = input(">")
    print("enter 0 to finish")