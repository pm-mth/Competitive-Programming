class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        w = 0
        while w < len(nums):
            if nums[w] > len(nums) or nums[w] == w + 1 or nums[w] <= 0:
                w += 1
            elif nums[nums[w] - 1] == nums[w]:
                w += 1
            else:
                nums[nums[w] - 1], nums[w] = nums[w], nums[nums[w]- 1]
        
 
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1