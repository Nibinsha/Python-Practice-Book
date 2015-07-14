import sys
x = sys.argv[1]
y = open(x).readlines()
for line in y:
    print line[::-1]
