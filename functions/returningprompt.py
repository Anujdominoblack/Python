import random
def get_integer(prompt):
    while True:
        temp=input(prompt)
        if temp .isnumeric():
            return int(temp)

highest=100
answer=random.randint(1,highest)
print(answer)
guess=0;
print("please guess the number between 1 and {}".format(highest))
while guess!=answer:
    guess=get_integer(":")  #this is the prompt argument it invokes the prompt

    if guess==0:
        break
    if guess==answer:
        print("well done you gueessed it")
    else:
        if guess<answer:
            print("guess answer")
        else:
            print("guess lower")
