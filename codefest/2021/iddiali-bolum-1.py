from sympy import divisors
from math import gcd

fedes_plays = True
tmp = input().split()
f, c = int(tmp[0]), int(tmp[1])


while True:
    if f == 1:
        print("Cee")
        break
    if c == 1:
        print("Fedes")
        break
    gcd_fc = gcd(f, c)
    if gcd_fc > 1:
        f, c = f // gcd_fc, c // gcd_fc
        fedes_plays = not fedes_plays
        continue
    if fedes_plays:
        f = divisors(f)[-2]
    else:
        c = divisors(c)[-2]

    fedes_plays = not fedes_plays
