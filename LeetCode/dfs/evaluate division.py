class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1/values[i]))
          
        
        def dfs(a, b):
            if a == b:
                return 1.0
            visited.add(a)

            ans = inf
            for neighbour, val in graph[a]:
                if neighbour not in visited:
                    ans = min (ans, dfs(neighbour, b) * val)
    
            return ans
        
        
        res = []
        for i in range(len(queries)):
            visited = set()
            if queries[i][0] not in graph or queries[i][1] not in graph:
                res.append(-1.0)
                continue
            ans1 = dfs(queries[i][0], queries[i][1]) 
            if ans1 == inf:
                res.append(-1.0)
            else:
                res.append(ans1)
        
    
        return res
