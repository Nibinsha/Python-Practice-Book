def main(file):
    x = open(file).read().split()
    f = {}
    for i in x:
        if i not in f:
           f[i] = 1
        else:
           f[i] = f[i] + 1
    for i,v in sorted(f.items()):
        print i,v

print main("string.txt")
