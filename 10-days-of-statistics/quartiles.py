#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Sort the array
    arr.sort()
    
    # Calculate Q2
    i = len(arr) // 2
    if len(arr) % 2 == 1:
        q2 = arr[i]
    else:
        q2 = (arr[i] + arr[i-1]) / 2
        
    # Define lower and higher halves
    low, high = arr[:i], arr[-i:]
    
    # Calculate Q1 and Q3
    i, j = len(low) // 2, len(high) // 2
    if len(low) % 2 == 1:
        q1 = low[i]
        q3 = high[j]
    else:
        q1 = (low[i] + low[i-1]) / 2
        q3 = (high[j] + high[j-1]) / 2
        
    return [int(q1), int(q2), int(q3)]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
