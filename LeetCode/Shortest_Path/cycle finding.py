from collections import defaultdict
from math import inf
def inp():
    return(int(input()))
    
def inlt():
    return(list(map(int,input().split())))
    
def insr():
    s = input()
    return(list(s[:len(s)]))
 
def invr():
    return(map(int,input().split()))
 
n, m = invr()
graph = []
for _ in range(m):
    a, b, c = invr()
    graph.append([a, b, c])
 
dist = [float(inf) for node in range(n + 1)]
is_cycle = False
res = []
parent = [0] * n
flag = False
for _ in range(1, n):
    for u, v, w in graph:
        if dist[u] == float(inf):
            dist[u] = 0
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            parent[v -1] = u - 1
 
    
for u, v, w in graph:
    if dist[u] == float(inf):
        dist[u] = 0
    if dist[u] + w < dist[v]:
        parent[v-1] = u - 1
        is_cycle = True
        index = u - 1
        break
 
 
position  = defaultdict(int)
while is_cycle:
    if parent[index]  + 1 in position:
        res.append(parent[index] + 1)
        i = position[parent[index] + 1]
        break
 
    res.append(parent[index] + 1)
    position[parent[index] + 1] = len(res) - 1
    index = parent[index]
    
 
  
if is_cycle:
    print("YES")
    print(*reversed(res[i:]))            
    
else:
    print("NO")
