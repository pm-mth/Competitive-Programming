class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def good(k):
            hours = 0
            for i in range(len(piles)):
                hours += ceil(piles[i]/k)
            
            return hours
        
        left, right = 0, max(piles) + 1
        
        while right > left + 1 :
            mid = left + (right - left)//2
            
            if good(mid) <= h:
                right = mid
            else:
                left = mid
                
        return right
                
        
        
       
        