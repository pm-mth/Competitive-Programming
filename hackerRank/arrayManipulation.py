#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    prefix = [0] * (n + 1)
    for query in queries:
        prefix[query[0] - 1] += query[2]
        prefix[query[1]] -= query[2]
        
    max_value =prefix[0]
    for r in range(1, len(prefix) -1):
        prefix[r] = prefix[r-1] + prefix[r]
        max_value = max(max_value, prefix[r])
        
    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
