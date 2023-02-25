name=input("enter your name")
age=int(input("enter your age"))
if age>18:
    print("please vote ")
elif age<18:
    print("please come back after {0}".format(18-age))
else:
    print("oh wow you are exactly 18")