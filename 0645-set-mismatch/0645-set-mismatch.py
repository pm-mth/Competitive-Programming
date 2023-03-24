class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if nums[i] == i + 1 or nums[i] == nums[nums[i] - 1]:
                i += 1
            else:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return [nums[i], i + 1]
            
        