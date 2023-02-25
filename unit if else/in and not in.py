parrot="Norwegian Blue"
letter=input("enter the character letter you want to check")
if letter in parrot.casefold():  #in check for boolean value if it is present or not
    print("{} is in {}".format(letter,parrot))  #output
else: #if boolean evaluates to false
    print("{} is not in {}".format(letter,parrot))  #output