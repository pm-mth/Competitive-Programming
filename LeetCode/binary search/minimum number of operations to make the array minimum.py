class Solution:
    def minOperations(self, nums: List[int]) -> int:
        r  = len(nums)
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        cost = inf
        for i in range(len(nums)):
            n = nums[i] + r
            index = bisect_left(nums, n)
          
            cost = min(cost, i + (r - (index))) 
        
        return cost

        
