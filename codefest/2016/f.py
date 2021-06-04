z = input()  # filler code
z = input().split()
s = [int(i) for i in z]
s.sort()
result = 0
for x in range(len(s) - 2):
    for y in range(x+1, len(s) - 1):
        for z in range(y+1, len(s)):
            if s[z] >= s[x] + s[y] and s[x] <= s[z] - s[y]:
                break
            else:
                result += 1
print(result)
