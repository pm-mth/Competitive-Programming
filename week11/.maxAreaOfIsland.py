class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m  = len(grid)
        n = len(grid[0])
        visited = set()
        maximum = 0
        
        def dfs(r,c):
            if r < 0 or c < 0 or r >= m or c >=n:
                return 0
            if grid[r][c] == 0:
                return 0
            if (r,c) in visited:
                return 0
            
            visited.add((r,c))
            size = 1
            size += dfs(r+1, c)
            size += dfs(r-1, c)
            size += dfs(r, c+1)
            size += dfs(r, c -1)
            
            return size
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    maximum  = max(maximum, dfs(row, col))
        return maximum
