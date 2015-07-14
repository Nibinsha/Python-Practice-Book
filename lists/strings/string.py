a = "Hello Nib,insha"
print a[:]
print a[2:]
print a[:2]
print a[:-1]
print a[::-1]
print "=============================================="
print a.split(",")
print "join===================================="
b = "hello Nibinsha"
x = b.split()
z = " "
print z.join(a)
print "strip =========================================="
q = a.strip("Hello")
print q
print "add ============================================="
print "%r%r"%(q,a)
