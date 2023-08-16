class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [nums[i] - nums[i - 1] for i in range(1, len(nums)) if nums[i] - nums[i -1] != 0] 

        if not dp:
            return 1
        
        count = 2
        for i in range(1, len(dp)):
            if dp[i] > 0 and dp[i - 1] < 0 or dp[i - 1] > 0 and dp[i] < 0:
                count += 1
        return count
       
