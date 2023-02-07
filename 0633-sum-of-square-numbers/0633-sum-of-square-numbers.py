class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        limit = ceil(c**0.5)
        
        left = 0
        right = limit
        
        while left <= right:
            cur = left**2 + right**2
            if cur == c:
                return True
            elif cur < c:
                left += 1
            else:
                right -= 1
        return False
            
        