def strlist(l):
    a = []
    for i in l:
        if i not in a:
           a.append(i)
    return a
print strlist(["python","java","python","java"])
