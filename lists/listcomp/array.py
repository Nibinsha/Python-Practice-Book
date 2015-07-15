def array(x,y):
    p = range(x)
    q = range(y)
    a = [[None for i in p]for j in q]
    a[0][0] = 5
    print a
array(3,2)
