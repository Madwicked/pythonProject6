d = {}
def update_dictionary(d,key,value):
    if key in d:
        d[key].append(value)
    else:
        if 2*key in d:
            d[2*key].append(value)
        if 2*key not in d:
            d[2*key]=[value]



update_dictionary(d,0,-5)
print(d)
update_dictionary(d,1,-1)
print(d)
update_dictionary(d,2,-2)
print(d)
update_dictionary(d,3,-3)
print(d)