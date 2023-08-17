class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        answer = [[inf]* n for i in range(n)]
        dirc  = [(1, -1), (1, 0), (1, 1)]
        
        def isValid(r, c):
            return 0 <= r < n and 0 <= c < n
        
        res = inf
        for r in range(n -1, -1, -1):
            for c in range(n):
                for i, j in dirc:
                    if isValid(r + i, c + j):
                        answer[r][c] = min(answer[r][c], answer[r + i][c + j])


                if answer[r][c] == inf:
                    answer[r][c] = matrix[r][c]
                else:
                    answer[r][c] += matrix[r][c]
                if r == 0:
                    res = min(res, answer[r][c])
    
        return res

        
