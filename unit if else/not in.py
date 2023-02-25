parrot="Norwegian blue"
letter=input("enter the letter you want to check")
if letter not in parrot.casefold(): #.casefold() converts the lowercase to uppercase
    print("{} is not in {}".format(letter,parrot))  #output
else:
    print("{} is in {}".format(letter,parrot))  #output