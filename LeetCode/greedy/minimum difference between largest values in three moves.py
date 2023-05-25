class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        nums.sort()
        a = nums[-1] - nums[3]
        b = nums[-4] - nums[0]
        c = nums[-2] - nums[2]
        d = nums[-3] - nums[1]
        
        return min(a, b, c, d)
