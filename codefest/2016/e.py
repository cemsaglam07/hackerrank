commands = []
friends = []
setcommand = set()


def belongs(u_b, v_b):
    for i_b, f in enumerate(friends):
        if u_b in f or v_b in f:
            return i_b
    return -1


zzz = input()
n, m = map(int, zzz.split())

if m == 0:
    import sys
    print(1, 1)
    sys.exit()

for _ in range(m):
    zzz = input()
    u, v = map(int, zzz.split())
    commands.append((u, v))
    setcommand.add(u)
    setcommand.add(v)
    

early = set(range(1, n)) - setcommand
if len(early) != 0:
    print(min(early), 1)
    import sys
    sys.exit()

for u, v in commands:
    i = belongs(u, v)
    if i == -1:
        friends.append({u, v})
    else:
        friends[i].add(u)
        friends[i].add(v)


for i in range(len(friends)):
    for j in range(i+1, len(friends)):
        if friends[i] & friends[j]:
            friends[i] = friends[i] | friends[j]
            friends[j] = set()


res = []
minr = float("inf")
for i, ff in enumerate(friends):
    lenff = len(ff)
    if lenff == 0 or lenff > minr:
        continue
    if lenff == minr:
        res.append(i)
    elif lenff < minr:
        minr = lenff
        res = [i]

rfr = set()
for i in res:
    rfr |= friends[i]
print(min(rfr), minr)
