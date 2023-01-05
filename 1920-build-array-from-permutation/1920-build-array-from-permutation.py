class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        permutation = []
        
        for i in range(len(nums)):
            permutation.append(nums[nums[i]])
        return permutation
        
        
        