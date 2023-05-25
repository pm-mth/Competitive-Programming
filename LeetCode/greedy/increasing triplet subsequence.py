class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        low, mid = inf, inf
        for i in range(len(nums)):
            if nums[i] > mid:
                return True
            
            if nums[i] < low:
                low = nums[i]
            if nums[i] > low and nums[i] < mid:
                mid = nums[i]
                
        return False
