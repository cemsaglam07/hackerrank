import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos, neg, zero = 0, 0, 0
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        elif num == 0:
            zero += 1
    n = pos + neg + zero
    print(format(pos/n, ".6f"))
    print(format(neg/n, ".6f"))
    print(format(zero/n, ".6f"))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
