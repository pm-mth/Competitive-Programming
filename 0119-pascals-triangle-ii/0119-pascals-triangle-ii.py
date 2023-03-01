class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def find(n):
            #base case
            if n == 0:
                return [1]
            
            down = find(n-1)
            
            temp = [1]*(n+1)
            for r in range(1, n):
                temp[r] = down[r-1] + down[r]
            
            return temp
        return find(rowIndex)
            
        