def word(file):
    f = {}
    x = open(file).read().split()
    for i in x:
        if i not in f:
           f[i] = 1
        else:
           f[i] = f[i] +1
    for k,v in sorted(f.items(),reverse=True):
        print k,v

word("string.txt")
