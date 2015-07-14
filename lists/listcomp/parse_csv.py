import re
def parse(f):
    x = open(f).readlines()
    a = []
    for i in x:
        s = re.findall('\w+',i)
        a.append(s)
    print a
parse("text.txt")
