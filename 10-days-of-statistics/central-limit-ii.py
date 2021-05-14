# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def main():
    x, n, mean, std = [float(input()) for i in range(4)]
    print(round(phi(x, n * mean, math.sqrt(n) * std), 4))


def phi(x, u, o):
    return (1.0 + math.erf(
        (x - u) / (o * math.sqrt(2.0))
    )) / 2.0


main()
