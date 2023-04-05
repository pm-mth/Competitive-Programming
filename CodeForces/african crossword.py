#import sys
from collections import defaultdict
from collections import Counter
#import math

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))

def insr():
    s = input()
    return(list(s[:len(s)]))

def invr():
    return(map(int,input().split()))

row, col = invr()
matrix = []
count_row = []
count_col = []

for _ in range(row):
     newR = input()
     matrix.append(newR)

for i in range(row):
    count_row.append(Counter(matrix[i]))
    for j in range(col):
        if len(count_col) <= j:
            count_col.append(Counter(matrix[i][j]))
        else:
            count_col[j].update(Counter(matrix[i][j]))
ans = ""
for i in range(row):
    for j in range(col):
        if count_row[i][matrix[i][j]] > 1 or count_col[j][matrix[i][j]] > 1:
            continue
        ans += matrix[i][j]
print(ans)
        
     
    
