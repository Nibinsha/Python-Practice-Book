def grplist(l,size):
    leng = len(l)
    new = []
    for i in range(0,leng):
        for j in range(i,size):
            new[i].append(l[j])
    print new
grplist([1,2,3,4,5,6,7,8,9],3)
