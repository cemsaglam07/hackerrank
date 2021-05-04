# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = sorted(list(map(int, input().split())))

# Calculate mean
print(sum(x) / n)

# Calculate median
print(x[n // 2] if n % 2 == 1 else (x[n // 2] + x[n // 2 - 1]) / 2)

# Calculate mode
m = {i: 0 for i in x}
for i in x:
    m[i] += 1
print(max(m, key=lambda k: m[k]))
