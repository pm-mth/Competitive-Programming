class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        
        result = [[0 for _ in range(col - 2)  ] for _ in range(row -2)]
        
        direction = [(0,0),(0,1),(1,0),(1,1),(0,2),(2,0),(1,2),(2,1),(2,2)]
        for r in range(row-2):
            for c in range(col-2):
                max_value = 0
                for dirc in direction:
                    max_value = max(max_value, grid[r + dirc[0]][c + dirc[1]])
                result[r][c] = max_value
        return result
                    
        