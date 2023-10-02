class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        Graph = defaultdict(list)
        weight = defaultdict(int)
        for u, v in edges:
            Graph[u].append(v)
            Graph[v].append(u)
        
        
        
        def dfs(parent, node, too):
            if node == too:
                weight[too] += 1
                return True
            
        
            ans = False
            for neighbour in Graph[node]:
                if neighbour != parent:
                    ans = ans or dfs(node, neighbour, too)

            if ans:
                weight[node] += 1
            return ans
        
        
        for trip in trips:
            dfs(-1, trip[0], trip[1])
        
        @cache
        def dp(parent, node, half ):
            ans = 0
            for neighbour in Graph[node]:
                if neighbour != parent:
                    if half:
                        ans += dp(node, neighbour, not half) 
                    else:
                        ans += min(dp(node, neighbour, half),  dp(node, neighbour, not half)) 
                    
            if half:
                ans += (weight[node] * (price[node]//2))
            else:
                ans += (weight[node] * price[node])
    
        
            return ans
        
        
        return min(dp(-1, 0, True), dp(-1, 0, False))
                



        
        
        
