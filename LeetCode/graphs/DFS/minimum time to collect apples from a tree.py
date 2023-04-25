class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = defaultdict(list)
        visited = set()
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(u):
            nonlocal visited
            if graph[u] == []:
                if hasApple[u]:
                    return 2
                return 0
            
            visited.add(u)
            
            ans = 0
            for v in graph[u]:
                if v not in visited:
                    ans += dfs(v)
            if ans == 0 and hasApple[u]:
                return 2
            if ans == 0 and not hasApple[u]:
                return 0
            
            return ans + 2
        res = dfs(0)
        if res == 0:
            return 0
        
        return res - 2
            
        
