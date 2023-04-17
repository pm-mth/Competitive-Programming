from collections import defaultdict
while True:
    n = int(input())
    if n == 0:
        break
    e = int(input())
    graph = defaultdict(list)
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)


    color = [0] * n
    def dfs(graph, n):
        for u in range(1, n + 1):
            if color[u - 1] == 0:
                color[u - 1] = 1

            for v in graph[u]:
                if color[v - 1] == color[u - 1]:
                    return False
                color[v -1] = -1 * color[u - 1]
                
        return True
    


    if dfs(graph, n):
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")

    
        
