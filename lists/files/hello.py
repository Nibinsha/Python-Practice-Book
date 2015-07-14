import sys
print "number of arguments" , len(sys.argv),"arguments"
print "argumnets list",str(sys.argv)
for i in sys.argv:
    print i
x = open(i).read()
print x
