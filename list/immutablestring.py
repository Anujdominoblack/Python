result="you have passed the examination"
another_result=result
print(id(result))
print(id(another_result))
result="this is something new"
print(id(result))
print(id(another_result))