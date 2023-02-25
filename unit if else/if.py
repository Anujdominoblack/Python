age=int(input("enter your age"))
if age>=18:
    print("you are eligible for voting")
else:
    print("sorry you can't vote come after {0}".format(18-age))