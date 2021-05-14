# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial

fact = lambda x: factorial(x)

def b(x, n, p):
    return (fact(n) * (p ** x) * ((1.0 - p) ** (n-x))) / (fact(x) * fact(n-x))

    
def cdf(x, n, p):
    if type(x) == int:
        return b(x, n, p)
    
    elif (type(x) == range) or (type(x) == list):
        result = 0
        for r in x:
            result += b(r, n, p)
        return result
    

def main():
    perc, batch = map(int, input().split())
    # No more than 2 rejects
    print(round(cdf(range(0, 2+1), batch, perc / 100.0), 3))
    # At least 2 rejects
    print(round(cdf(range(2, batch+1), batch, perc / 100.0), 3))
    
    
main()
