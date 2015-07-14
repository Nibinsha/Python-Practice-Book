import sys
x = sys.argv[1]
y = open(x).readlines()
for line in reversed(y):
    print line
