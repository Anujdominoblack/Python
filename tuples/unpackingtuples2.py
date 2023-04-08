for t in enumerate("abcdefgh"):
    print(t)   #it returns a tuple
index,character=(0,"a")
print(index)
print(character)
# another way of unpacking
for t in enumerate("abcdefgh"):
    index,character=t
    print(index,character)

for m in enumerate("qwertyuiop"):
    index,character=m
    print(index,character)