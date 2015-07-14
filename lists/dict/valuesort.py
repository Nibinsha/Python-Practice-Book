def value(d):
    f = []
    for i,v in sorted(d.items()):
        f.append(v)
    print f

value({'x':1,'y':2,'a':3})
