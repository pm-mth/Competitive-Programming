class Solution:
    def mySqrt(self, x: int) -> int:
        low , high = 0, x
        
        while low <= high:
            mid = low + (high - low)//2
            square = mid ** 2
            
            if square == x:
                return mid
            elif square < x:
                low = mid + 1
                if low ** 2 > x:
                    return low - 1
            elif square > x:
                high = mid - 1
           
        return low 
        
        
            
        