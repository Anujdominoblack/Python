even=[2,4,6,8]
odd=[1,3,5,7]
even.sort()
odd.sort()
even.extend(odd)  #to append the odd list on the even list
print(even)
even.sort()
print(even)