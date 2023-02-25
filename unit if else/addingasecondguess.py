guess=5
answer=int(input("enter your answer"))
if guess<answer:
    print("please guess lower")
    answer=int(input())
    if answer==guess:
        print("congratulations you got that")
    else:
        print("ah ! you are wrong")
elif answer<guess :
    print("please guess higher")
    answer=int(input())
    if answer==guess:
        print("congrats")
    else:
        print("you are wrong")
else:
    print("you got in first chance")