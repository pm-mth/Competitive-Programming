class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        res = []
        for r in range(col):
            nw = []
            for c in range(row): 
                nw.append(matrix[c][r])
            res.append(nw)
                
        return res
        