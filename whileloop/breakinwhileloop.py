available=["north","south","east","west"]
choose=""
while choose not in available:  #looop runs until the condition is false
    choose=input("enter the choosen direction")
    if choose.casefold()=="quit":
        print("game over")
        break;
print("you are out")