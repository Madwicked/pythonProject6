l = [6,7,8,9,10]
#k=len(l)
l[:] = [i//2 for i in l if not i % 2]
#res = []
#for i in range(k):
    #if l[i] % 2 == 0:
        #l.append(l[i]//2)
    #else:
    #del l[i]
print(l)