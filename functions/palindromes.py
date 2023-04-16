def is_palindromes(string):  #string is taken as a input
    backwards=string[::-1]  #traversing the string backwards
    return backwards==string #it returns the boolean value true or false
print(is_palindromes("ABAC")) #function call

# making the case insenstive so that we get output based on alphabets and numeric not case
def palindromes(string):  #my solution
    return string[::-1]==string


if palindromes("Racecar".casefold()):
    print("yes")

#udemy solution

def palindromes2(string):
    return string[::-1].casefold()==string.casefold()

if palindromes2("Racecar"):
    print("yes")