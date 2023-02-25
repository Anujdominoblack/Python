age=int(input("enter your age"))
if age<18:
    print("please comeback in {0} years".format(18-age))
elif age==900:
    print("sorry yoda you have died in jedi")
else:
    print("you are old enough to vote")
    print("please cast your vote")