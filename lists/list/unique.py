def unique(L):
    a = []
    for i in L:
        if i not in a:
           a.append(i)
    print a
unique([1,2,2,3,4,4,5,5,5,5,6])
print "set() also"
print set([1,2,2,3,4,4,5,5,5,6])
