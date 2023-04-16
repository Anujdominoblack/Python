def fibbonaci(n):
    if 0<=n<=1:
        return n
    n1,n2=1,0
    result=None
    for i in range(1,n):
        result=n1+n2
        n2=n1
        n1=result
    return result


for i in range(1,35):
    print(i,fibbonaci(i))
