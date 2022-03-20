#with open('f:\.txt') as inf:
#    for line in inf:
#        line=line.strip()
s=input().sort().lower()
k=0
#    s_new=s[0]
for i in s:
    if s[i] == s[i+1]:
        k += 1
    else:
        s_new += s[i]
        s_new = ''.join(k)
        k=0
print(s_new)
