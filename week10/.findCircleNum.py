class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        flag = set()
        n = len(isConnected)
        province = 0
        
        def dfs(r):
            count = 0
            for c in range(n):
                if (r, c) in flag:
                    continue
                flag.add((r, c))
            
                if isConnected[r][c] == 1:
                    flag.add((c, r))
                    dfs(c)
                    count += 1
            return count
        for r in range(n):
            province += dfs(r)
        return province
            
                
            
