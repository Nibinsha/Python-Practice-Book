def dup(l):
    st= set()
    uniq = []
    for x in l:
        if x not in st:
           uniq.append(x)
           st.add(x)
    return uniq
print dup([1,2,3,4,4,45,5,6,7,7,8])
