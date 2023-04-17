class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
       
    
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def inbound(r, c):
            return 0 <= r < len(grid1) and 0 <= c < len(grid1[0])
        

        def dfs(i, j):
            nonlocal check
            if grid1[i][j] == 0:
                check = False
            
            grid2[i][j] = 0
            for r, c in directions:
                nr = i + r
                nc = j + c
                if inbound(nr, nc) and grid2[nr][nc] == 1:
                    dfs(nr, nc)
               
        
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                check = True
                if grid2[i][j] == 1:
                    grid2[i][j] = 0
                    dfs(i, j)
                    if check:
                        count += 1
        return count

                