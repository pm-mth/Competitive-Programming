from collections import defaultdict
def addEdge(u, v):
    graph[u].append(v)
    graph[v].append(u)

def vertex(u):
    print(*graph[u])

n  = int(input())
k = int(input())
graph = defaultdict(list)
for _ in range(k):
    num = list(map(int, input().split()))
    if num[0] == 1:
        addEdge(num[1], num[2])
    else:
        vertex(num[1])


