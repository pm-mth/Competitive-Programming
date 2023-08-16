class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for sub in range(n)]
        maxLength = 0

        for i in range(n - 2, -1, -1):
            for j in range(i+1, n):
                diff = nums[j] - nums[i]
               
                if diff in dp[i] and diff in dp[j]:
                    continue

                if not diff in dp[j]:
                    dp[j][diff] = 1
                if not diff in dp[i]:
                    dp[i][diff] = 1

                dp[i][diff] = max(dp[j][diff] + 1, dp[i][diff])
                maxLength = max(maxLength, dp[i][diff])
        
        return maxLength
                

    
