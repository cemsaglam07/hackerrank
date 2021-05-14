"""
# Useful information posted by ImAlexej
# Starting with this formula from the tutorial:
P(a <= X <= b) = P(a < X < b) = F_X(b) - F_X(a)

# If a is now 80 and b is infinity and X is the grade, we'll get:
P(80 <= grade <= inf) = P(80 < grade < inf) = F_X(inf) - F_X(80)

# Now we need to check the limit of the cumulative distribution function:
lim F_X(x) as x->infinity =>
lim (1/2 * (1 + erf(z))) as z->infinity = 1

With this information above we get:
P(80 < grade < inf) = P(grade > 80) = 1 - F_X(80)
"""

import math


def main():
    mean, std = map(int, input().split())
    high = int(input())
    passed = int(input())

    print(round((1 - phi(high, mean, std)) * 100, 2))
    print(round((1 - phi(passed, mean, std)) * 100, 2))
    print(round(phi(passed, mean, std) * 100, 2))


def phi(x, u, o):
    return (1.0 + math.erf(
        (x - u) / (o * math.sqrt(2.0))
    )) / 2.0


main()
