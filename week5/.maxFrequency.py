class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        overflow = 0
        count = 1
        
        for i in range(1, len(nums)):
            k -= (nums[i] - nums[i-1]) * (count - overflow)
            
            if k < 0:
                k += nums[i] - nums[overflow] 
                overflow += 1
                
            count += 1    
        
        return count - overflow
        
