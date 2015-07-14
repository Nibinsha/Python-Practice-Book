import sys
y = sys.argv[2]
x = open(sys.argv[1]).readlines()
for line in x:
    if y in line:
       print line
    
