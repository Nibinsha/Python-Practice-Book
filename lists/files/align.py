import sys
x = sys.agrv[1]
f = open(x).read()
l = []
p = []
for i in l:
    p.append(len(i))
print max(p)
for i in l:
    if len(i)<max(p):
       print " "*((max(p)-len(i))/2)+i
    else:
       print i
