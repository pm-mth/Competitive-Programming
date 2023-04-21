class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        answer = [1] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = set()
        def dfs(u):
            nonlocal visited
            if graph[u] == []:
                return defaultdict(int)
            
            visited.add(u)
            sameLabel = defaultdict(int)
            for v in graph[u]:
                if v not in visited:
                    ans = dfs(v)
                    for key in ans.keys():
                        sameLabel[key] += ans[key]
                    
            sameLabel[labels[u]] +=  1
            answer[u] = sameLabel[labels[u]]
            
            return sameLabel
        
        dfs(0)
        return answer
    
            
            
            
                
        
