from collections import defaultdict
n  = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

indegree = defaultdict(int)
outdegree = defaultdict(int)
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            indegree[j] += 1
            outdegree[i] += 1
sources = []
sinks = []
for i in range(n):
    if indegree[i] >= 0 and outdegree[i] == 0:
        sinks.append(i + 1)
    if outdegree[i] >= 0 and indegree[i] == 0:
        sources.append(i + 1)
    
sources.sort()
sinks.sort()
print(len(sources), *sources)
print(len(sinks), *sinks)




