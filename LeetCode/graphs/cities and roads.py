from collections import defaultdict
n  = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

count = 0
for i in range(n):
    for j in range(i+1, n):
        if matrix[i][j] == 1:
            count += 1
print(count)

