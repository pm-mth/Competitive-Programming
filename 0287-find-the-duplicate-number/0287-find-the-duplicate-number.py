class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i + 1 or nums[i] == nums[nums[i] - 1]:
                i += 1
            else:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return nums[-1]
#         for i in range(len(nums)):
#             if nums[i] != i + 1:
#                 return nums[i]
        