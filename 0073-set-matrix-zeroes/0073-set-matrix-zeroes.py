class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        set_row = set()
        set_col = set()
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    set_row.add(r)
                    set_col.add(c)
        
        for idx_r in set_row:
            for c in range(col):
                matrix[idx_r][c] = 0
        for idx_c in set_col:
            for r in range(row):
                matrix[r][idx_c] = 0
        