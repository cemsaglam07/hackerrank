# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
    x, y = [], [] 
    for i in range(5):
        tmp = input().split()
        x.append(float(tmp[0]))
        y.append(float(tmp[1]))
    
    # Find regression line
    m, n = regr_line(x, y)
    # Plug in values to y = mx + n
    print(round(m * 80 + n, 3))
    
    
def regr_line(x, y):
    m = p(x, y) * std(y) / std(x)
    n = mean(y) - (m * mean(x))
    return [m, n]
    
    
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
