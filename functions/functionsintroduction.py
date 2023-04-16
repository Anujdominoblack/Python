def multiply():  #the function that returns a value
    result=7*5
    return result
ans=multiply()  #function call without any argument
print(ans)

# function with paramter and that returns a value
def multiply1(x,y):
    result=x*y
    return result
ans1=multiply1(10,50)
print(ans1)

#function that does not return a value

def multiply2(x,y):
    result=x*y
    print(result)
multiply2(10,20) #function call