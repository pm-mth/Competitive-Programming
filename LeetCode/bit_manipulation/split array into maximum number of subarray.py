class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        score = nums[0]
        for i in range(1, len(nums)):
            score &= nums[i]
        if score > 0:
            return 1

        cur = nums[0]
        res = 0
        for i in range(1,len(nums)):
            if cur == score:
                res += 1
                cur = nums[i]
            cur &= nums[i]
            
        if cur == score:
            res += 1
   
        return res
        
