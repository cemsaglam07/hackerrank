# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
    n = int(input())
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))
    print(round(r(x, y), 3))


def r(x, y):
    d2, n = 0, len(x)
    for d_i in d(x, y):
        d2 += d_i ** 2
    return 1 - (6 * d2 / ((n-1)*(n)*(n+1)))
    
    
def d(x, y):
    rank_x, rank_y = rank(x), rank(y)
    return [rank_x[i] - rank_y[i] for i in range(len(x))]


def rank(arr):
    return [sorted(arr).index(i) + 1 for i in arr]


main()
