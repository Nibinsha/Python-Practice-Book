import re
def csv(f):
    x = []
    a = open(f).readlines()
    for i in a:
        r = i.replace("!","#")
        s = re.findall("\w+",r)
        x.append(s)
    print x
csv("a.txt")
