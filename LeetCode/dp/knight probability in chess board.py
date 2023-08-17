class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        dirc = [(-2,1), (-1,2), (2, 1), (1, 2), (2, -1), (1, -2), (-1,-2),(-2, -1)]
        
        
        def isValid(r, c):
            return 0 <= r < n and 0 <= c < n
        
        @cache

        def solve(r, c , k):
            if k == 0:
                return 1/8

            valid = 0
            for i, j in dirc:
                nr, nc = r + i, c + j
                if isValid(nr, nc):
                    valid += solve(nr, nc, k-1)
            
            return valid/8
           
       
        return  solve(row, column, k)* 8
                
            

