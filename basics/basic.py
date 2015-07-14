def sq(x):
    return x*x
def sum(x,y):
    return sq(x)+sq(y)

def add():
    return sq(3)+sum(4,5)
print sq(sq(3))+sq(4)
print sum(2,4)
print add()
