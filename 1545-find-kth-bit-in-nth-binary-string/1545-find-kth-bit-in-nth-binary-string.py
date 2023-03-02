class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        bits = {'0': '1', '1': '0'}
        
        def solve(n):
            if n == 1:
                return "0"
            
            below = solve(n - 1)
         
            inverse = ""
            for i in below:
                inverse += bits[i]
        
            reverse = inverse[::-1]
    
            return below + "1" + reverse

        return solve(n)[k - 1]
        