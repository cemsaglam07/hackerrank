import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    if n > 0:
        for i in range(n):
            p = " " * (n-i-1)
            p += "#" * (i+1)
            print(p)
            
    
if __name__ == '__main__':
    n = int(input())

    staircase(n)
