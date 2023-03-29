class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #cyclic sort
        res = 0
        n = len(nums)
        for i in range(n + 1):
            res ^= i
        
        for i in range(n):
            res ^= nums[i]
        
        return res
    

        
        
       