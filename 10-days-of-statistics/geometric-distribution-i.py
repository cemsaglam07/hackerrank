# Enter your code here. Read input from STDIN. Print output to STDOUT
def g(n, p):
    return ((1-p) ** (n-1)) * p

num, den = map(int, input().split())
no = int(input())
print(round(g(no, num/den), 3))
