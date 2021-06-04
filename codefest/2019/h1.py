import re


ss = re.findall(r'[0-9]+[fg]+', input().strip())
z = set()
for s in ss:
    for i in range(len(s)):
        if s[i] in ["g", "f"]:
            z.add(s[:i+1])

print(len(z))
