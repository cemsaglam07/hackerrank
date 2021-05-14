# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
    n = int(input())
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))
    print(round(p(x, y), 3))


def p(x,y):
    u_x, o_x, u_y, o_y = mean(x), std(x), mean(y), std(y)
    count = 0
    for i in range(len(x)):
        count += (x[i] - u_x) * (y[i] - u_y)
    return count / (len(x) * o_x * o_y)

    
def mean(arr):
    return sum(arr) / len(arr)


def std(arr):
    u = mean(arr)
    return (sum([(i - u) ** 2 for i in arr]) / len(arr)) ** 0.5


main()
