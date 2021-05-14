def main():
    a, b = map(float, input().split())
    print(round(160 + (40 * x_2(a)), 3))
    print(round(128 + (40 * x_2(b)), 3))


def x_2(x):
    return x * (1 + x)


main()
