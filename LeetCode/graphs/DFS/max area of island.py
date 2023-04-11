class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [(0, 1), (1,0), (0,-1), (-1,0)]
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(i, j):
            if not inbound(i, j):
                return 0
            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            ans = 0
            for r, c in direction:
                nr = i + r
                nc = j + c
                ans += dfs(nr, nc)

            return ans + 1
        max_val = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_val = max(max_val, dfs(r, c))
        return max_val

            
