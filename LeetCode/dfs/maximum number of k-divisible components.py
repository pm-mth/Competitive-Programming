class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        res = 0
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[v] += 1
            indegree[u] += 1
        root = 0
        for i in range(n):
            if indegree[i] == 4:
                root = i
        graph[root].append(-1)
       
        def dfs(parent, node):
            nonlocal res
           
            if len(graph[node]) == 1:
                if values[node] % k == 0:
                    res += 1
                    return 0
                return values[node]
            
            add = 0
            for neighbour in graph[node]:
                if parent != neighbour:
                    add += dfs(node, neighbour)

            add += values[node]
            if add %k == 0:
                res += 1
                return 0
            return add
        dfs(-1, root)
        return res
            

            
        
