# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import e
from math import factorial

def p(k, v):
    return (v ** k) * (e ** (-v)) / factorial(k)


def main():
    v = float(input())
    k = int(input())
    print(round(p(k, v), 3))
    
    
main()
