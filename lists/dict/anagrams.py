def anag(l):
    d = {}
    for i in l:
        print sorted(i)
        s = " ".join(sorted(i))
        if s not in d:
           d[s] = []
        d[s].append(i)
    print d.values()

anag(["eat","ate","tea","kite","keit"])
