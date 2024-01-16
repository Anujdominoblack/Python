# it provides set of items prsent in one set but not in another

morning = {'java','c','ruby','swift','csharp',}

afternoon = {'python','csharp','java','c','ruby',}

possible_courses = morning^afternoon

print(possible_courses)

courses = afternoon^morning
print(courses)

# here we can see that symmetric difference is commutative 