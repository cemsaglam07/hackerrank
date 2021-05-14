# Enter your code here. Read input from STDIN. Print output to STDOUT
def g(n, p):
    return ((1-p) ** (n-1)) * p


def main():
    num, den = map(int, input().split())
    no = int(input())
    
    result = 0
    for r in range(1, no+1):
        result += g(r, num/den)
    print(round(result, 3))
    
    
main()
