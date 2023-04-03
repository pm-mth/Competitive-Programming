#import sys
#from collections import defaultdict

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))

def insr():
    s = input()
    return(list(s[:len(s)]))

def invr():
    return(map(int,input().split()))

test_case = inp()
for _ in range(test_case):
    row, col = invr()
    matrix = []
    for _ in range(row):
        matrix.append(inlt())
    left_sum = [0] * (row  + col - 1)
    right_sum = [0] * (row  + col  - 1)
    for r in range(row):
        for c in range(col):
            left_sum[r - c + col - 1] +=  matrix[r][c]
            right_sum[r + c] += matrix[r][c]
    
    max_val = 0
    for r in range(row):
        for c in range(col):
            max_val = max(max_val, left_sum[r - c + col - 1] + right_sum[r + c] - matrix[r][c])
    
    print(max_val)
            
