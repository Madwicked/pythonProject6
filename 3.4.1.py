s=[] #f4v12V9u19y16C2m20
k=[]
d=0
a=0

with open('F:\dataset_3363_2.txt') as inf:
    for line in inf:
        line=line.strip()
    s=str(line)
#s = input()

    l=len(s)
    i=0
    for i in range(l-1):
        if s[i]>='A':
            k += s[i]
            j=s[i]
        elif s[i] < 'A' and s[i - 1] < 'A':
            i += 1
        elif s[i] < 'A': #and s[i+1] < 'A':
            d = ''.join(s[i])
            if s[i+1] < 'A':
                d +=s[i+1]
            d=int(d)
            k += j*(d-1)
   # elif s[i] < 'A':
   #     d = int(s[i])
   #     if d > 1:
   #         k += j * (d - 1)
    a = ''.join(k)
#print(k)

with open('F:\dz.txt', 'w') as ouf:
    ouf.write(a)
