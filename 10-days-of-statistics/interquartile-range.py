#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    # Sort the array
    arr = [values[i] for i in range(len(freqs)) for j in range(freqs[i])]
    arr.sort()
    
    # Define lower and higher halves
    i = len(arr) // 2
    low, high = arr[:i], arr[-i:]
    
    # Calculate Q1 and Q3
    i, j = len(low) // 2, len(high) // 2
    if len(low) % 2 == 1:
        q1 = low[i]
        q3 = high[j]
    else:
        q1 = (low[i] + low[i-1]) / 2
        q3 = (high[j] + high[j-1]) / 2
        
    print(f"{q3-q1:.1f}")

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
