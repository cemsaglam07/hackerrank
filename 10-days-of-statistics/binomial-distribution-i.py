# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial

def fact(x):
    return factorial(x)

    
def b(x, n, p):
    return (fact(n) * (p ** x) * ((1.0 - p) ** (n-x))) / (fact(x) * fact(n-x))

    
def cdf(x, n, p):
    result = 0
    for r in range(x, n+1):
        result += b(r, n, p)
    return result

    
def main():
    boy, girl = map(float, input().split())
    print(round(cdf(3, 6, boy/(boy+girl)), 3))

main()
