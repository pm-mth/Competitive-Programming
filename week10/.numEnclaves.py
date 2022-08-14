class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] != 1:
                return 
           
            grid[r][c] = 0
            for dirc in ([1, 0], [0, 1], [-1, 0], [0, -1]):
                nr = r + dirc[0]
                nc = c + dirc[1]
                dfs(nr, nc)
            
           
            
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row in [0, m - 1] or col in [0, n - 1]):
                    dfs(row, col)
        count = 0
        for row in range(m):
            for col in range(n):
                count += 1 if grid[row][col] == 1 else 0
        return count
