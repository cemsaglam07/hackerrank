#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    moves = [0]
    while moves[-1] != (len(c)-1):
        try:
            if c[moves[-1] + 2] == 0:
                moves.append(moves[-1] + 2)
                continue
        except IndexError:
            try:
                if c[moves[-1] + 1] == 0:
                    moves.append(moves[-1] + 1)
                    continue
            except IndexError:
                return len(moves)-1
        try:
            if c[moves[-1] + 1] == 0:
                moves.append(moves[-1] + 1)
                continue
        except IndexError:
            return len(moves)-1
    return len(moves)-1
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
