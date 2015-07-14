def inv(d):
    f = {}
    print dict(map(reversed,d.iteritems()))
    
inv({'x':1,'y':2,'z':3})
