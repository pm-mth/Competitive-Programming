class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def divisor(nums, x):
            add = 0
            for i in range(len(nums)):
                if x:
                    add += ceil(nums[i]/x)
            
            return add
        
        left, right = 0, max(nums) + 1
        
        while right > left + 1:
            mid = left + (right - left)//2
            
            if divisor(nums, mid) > threshold:
                left = mid
            else:
                right = mid
        
        return right
                
        