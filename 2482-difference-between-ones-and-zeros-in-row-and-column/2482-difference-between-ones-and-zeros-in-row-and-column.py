class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        row_count = defaultdict(int)
        col_count = defaultdict(int)
        
        for r in range(rows):
            for c in range(cols):
                row_count[(r, grid[r][c])] += 1
                col_count[(c, grid[r][c])] += 1
        
        diff = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                diff[r][c] = (row_count[(r, 1)] +  
                              col_count[(c, 1)] - 
                              row_count[(r, 0)] - 
                              col_count[(c, 0)])
        return diff
                