# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np


def main():
    m, n = map(int, input().split())
    x, y = [], []
    for _ in range(n):
        tmp = [1.0] + list(map(float, input().split()))
        x.append(tmp[:m + 1])
        y.append(tmp[m + 1:])
    x = np.array(x)
    y = np.array(y)

    b = find_b(x, y)

    q = int(input())
    find_x = []
    for _ in range(q):
        find_x.append([1.0] + list(map(float, input().split())))

    for fset in find_x:
        fset = np.array(fset)
        print(float(fset @ b))


def find_b(x, y):
    # Find T(X), the transpose of X
    xt = x.transpose()
    # Find the matrix multiplication of T(X) and X
    xt_x = xt @ x
    # Find the inverse of the T(X) * T
    xt_x_inv = np.linalg.inv(xt_x)
    # Find (T(X) * X)^-1  * T(X)
    xt_x_inv_x = xt_x_inv @ xt
    # Find (T(X) * X)^-1  * T(X) * Y
    return xt_x_inv_x @ y


main()
