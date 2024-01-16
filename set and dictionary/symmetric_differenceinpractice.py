# the advantage of method is that we can pass any iterable so that

morning = ['java','c','ruby','swift','csharp',]

afternoon = ['python','c#','java','c','ruby']

possible_courses = set(morning).symmetric_difference(afternoon) # in method we can pass any iterable
print(possible_courses)  # output

# courses = morning^afternoon  # it will throw an error as operand is not allowed
# print(courses)