class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        nums.append(float("inf"))
        while i < len(nums):
            if nums[i] == float("inf") or nums[i] == i:
                i += 1
            else:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        for i in range(len(nums)):
            if nums[i] == float("inf"):
                return i
                
        
        
        
        
       