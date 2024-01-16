# choice = "-"
# while choice != '0':
     #if choice in list("12345"):
         #print("you choose {}".format(choice))
     #else:
         #print("please choose your option from below")
         #print("1:\t learn python")
         #print("2:\t learn java")
         #print("3:\t go swimming ")
         #print("4:\t have dinner" )
         #print("5:\t go to bed ")

     #choice = input(">>>>>")



# now doing the same thing using set

choice = "-"
while choice != '0':
    if choice in set("12345"):
        print("you choose {}".format(choice))
    else:
        print("please choose your option from below")
        print("1:\t learn python")
        print("2:\t learn java")
        print("3:\t go swimming ")
        print("4:\t have dinner" )
        print("5:\t go to bed ")

    choice = input(">>>>>")