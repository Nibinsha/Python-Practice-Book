def triplet(a):
    print [(x,y,z) for x in range(1,a) for y in range(x,a) for z in range(y,a) if (x+y) == z ]

triplet(5)
