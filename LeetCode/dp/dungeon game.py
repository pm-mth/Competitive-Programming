class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        res = inf

        dirc = [(0,1),(1, 0)]
        r, c = len(dungeon), len(dungeon[0])

        def inbound(r, c):
            return 0 <= r < len(dungeon) and 0 <= c <len(dungeon[0])

        
        @cache
        def solve(i, j):
            if (i,j) == (r -1, c -1):
                return min(0, dungeon[i][j])
            
            val = -inf
            for row, col in dirc:
                if inbound(row + i, col + j):
                    val = max(val,solve(row + i, col + j))
            
            return min(val + dungeon[i][j], 0)
            
        return 1 - solve(0, 0)

        
                

