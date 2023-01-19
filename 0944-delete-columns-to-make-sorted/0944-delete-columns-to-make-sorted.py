class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        number_of_col = 0
        for j in range(len(strs[0])):
            for i in range(len(strs)-1):
                if strs[i][j] > strs[i+1][j]:
                    number_of_col += 1
                    break
        return number_of_col
                    
                
                
            
        