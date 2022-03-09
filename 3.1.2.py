#l = [1, 2, 3, 4, 5, 6]
def modify_list(l):
    l[:] = [i//2 for i in l if not i % 2]

    return l
    print(l)

modify_list([10,5,8,3])