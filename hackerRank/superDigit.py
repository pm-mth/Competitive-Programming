#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    p = n
    def calculate_super_digit(p,k):
        if len(p) == 1:
            return int(p)
        
        add = 0
        for r in range(len(p)):
            add += int(p[r])
        if int(k):
            add *= int(k)
        k = 0
        return calculate_super_digit(str(add), str(k))
    
    return calculate_super_digit(p, k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
