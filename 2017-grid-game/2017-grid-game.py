class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        preSum = [[0]*col for _ in range(row)]
        
         #first row
        preSum[0][col - 1] = grid[0][col - 1]
        for i in range(col-2, -1, -1):
            preSum[0][i] = grid[0][i] + preSum[0][i + 1]
        
        #second row
        preSum[1][0] = grid[1][0]
        for i in range(1, col):
            preSum[1][i] = grid[1][i] + preSum[1][i - 1]
        
        r, c = 0, 0
        while c < col:
            grid[r][c] = 0
            
            if not r and (c == col - 1 or preSum[r+1][c] > preSum[r][c+ 1]):
                r += 1
            else:
                c += 1
        
        return max(sum(grid[0]), sum(grid[1]))
            
            
        
        
            
        
       
        
        
        
        
        
        