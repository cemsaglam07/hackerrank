x, y = [int(i) for i in input().split()]
if (x == y):
    print("MUMKUN")
    print(0)
else:
    r = True
    for i in range(len(bin(x)) - len(bin(x).rstrip('0'))):
        x = x >> 1
        if x == y:
            r = False
            print("MUMKUN")
            print(i + 1)
            break
    if r:
        print("MUMKUN DEGIL")
