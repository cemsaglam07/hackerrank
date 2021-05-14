import math


def phi(x, u, o):
    return (1.0 + math.erf(
        (x - u) / (o * math.sqrt(2.0))
    )) / 2.0


def main():
    mean, std = map(int, input().split())
    q1 = float(input())
    a, b = map(int, input().split())

    print(round(phi(q1, mean, std), 3))
    print(round(phi(b, mean, std) - phi(a, mean, std), 3))


main()
