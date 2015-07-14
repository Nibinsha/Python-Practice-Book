d = {1:'a','w':2,'d':3}
print d.keys()
print d.values()
print d.items()
d[3] = "foo"
print d
del d[1]
print d
print "=============================================================="
print "=================================================================="
for key in d:
    print key
for k,v in d.items():
    print k,v
print "============================================================"
print "has_key or in ============================================================"
print d.has_key('w')
print "=========================================================="
print "get and setdefault ======================================"
s = {'a':1,'q':2,'e':3}
print s.get('a',5)
d.setdefault('w',0)
print s
print "==============================================================="
w = {"hello" : "nibin"}
print "hiii %(hello)s" %w
