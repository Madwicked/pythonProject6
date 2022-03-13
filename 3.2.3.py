n = int(input())
k=0
d={}
while k<=n:
    x=int(input())
    k+=1
    if x not in d:
        d[x]=f(x)
    print(d(x))