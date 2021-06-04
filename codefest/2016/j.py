result = ""
s = int(input())
a = input().strip()
b = input().strip()
c = input().strip()
d = input().strip()
e = input().strip()

for i in range(s):
    x = sorted((a[i], b[i], c[i], d[i], e[i]))
    if x == ['A', 'B', 'B', 'C', 'C']:
        result += "A"
    elif x == ['A', 'A', 'B', 'C', 'C']:
        result += "B"
    elif x == ['A', 'A', 'B', 'B', 'C']:
        result += "C"
print(result)
