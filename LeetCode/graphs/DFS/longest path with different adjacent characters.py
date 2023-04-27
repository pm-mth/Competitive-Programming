class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        answer = 0
        graph = defaultdict(list)
        visited = set()
        
        for i in range(len(parent)):
            graph[parent[i]].append(i)
    
        def dfs(u, prev):
            nonlocal answer
                  
            max_path_1 , max_path_2 = 0, 0
            for v in graph[u]:
                res = dfs(v, s[v])
                if s[v] != prev:
                    if res > max_path_1:
                        max_path_2 = max_path_1
                        max_path_1 = res
                    elif max_path_1 >= res > max_path_2:
                        max_path_2 = res
    
            answer = max(answer, max_path_1 + max_path_2 + 1)
            
            return max_path_1 + 1
        
        dfs(0, s[0])
        
        return answer
                
        
        
        
        
