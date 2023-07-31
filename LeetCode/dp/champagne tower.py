class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0
        
        if query_row == 0:
            return 1

        prev = [poured]
        for i in range(1, query_row + 1):
            glasses = [0] * (i + 1)
            for j in range(i + 1):
                if j == 0:
                    prev_glass = prev[j] - 1
                    if prev_glass < 0:
                        prev_glass = 0
                    glasses[j] = prev_glass * 0.5
                elif j == i:
                    prev_glass = prev[j -1] - 1
                    if prev_glass < 0:
                        prev_glass = 0
                    glasses[j] = prev_glass * 0.5 
                else:
                    prev_glass1 = prev[j -1] - 1
                    if prev_glass1 < 0:
                        prev_glass1 = 0
                    prev_glass2 = prev[j] - 1
                    if prev_glass2 < 0:
                        prev_glass2 = 0
                    glasses[j] = prev_glass1 * 0.5 + prev_glass2 * 0.5

            prev = glasses
        
        if glasses[query_glass] <= 1:
            return glasses[query_glass]
        else:
            return 1
                
            
