low=1
high=1000
print("please think  a number between {} and  {} ".format(low,high))
input("press enter to start")
guesses=0;
while True: #we got it because we dont need the loop condition here
    guess=low+(high-low)//2
    cguess=input("my guess is {} .please press h for high guess"
                 "press l for guessing lower and press c is my guess is correct"
                 .format(guess)).casefold()
    if cguess=='h':
        low=guess+1
    elif cguess=='l':
        high=guess-1
    elif cguess=='c':
        print("i got it in {} guessess".format(guesses))
        break
    else:
        print("please enter h l or c")
    guesses=guesses+1


