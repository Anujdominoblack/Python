answer=5
guess=int(input("enter the guessed number"))
if guess!=answer :
    if guess<answer:
        print("please guess higher")
    else:
        print("please guess lower")
    guess=int(input())
    if guess==answer:
        print("congrats you got that")
    else:
        print("you lost that")
else:
    print("wow in first chance")