from collections import Counter

no = input()
data = input().split()

anagram = map(lambda x: "".join(sorted(x)), data)

c = dict(Counter(anagram))

count = 0
for v in c.values():
    # n! / (r! * (n-r)!)
    # n! / (2! * (n-2)!)
    # n * n-1 * n-2! / (2! * n-2!)
    # n * n-1 / 2!
    if v == 1:
        count += 0
        continue
    elif v == 2:
        count += 1
        continue
    count += (v * (v - 1)) / 2

print(int(count))
