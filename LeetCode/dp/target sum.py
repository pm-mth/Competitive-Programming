class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dp(i, exp):
            if i >= n:
                if target == exp:
                    return 1
                
                return 0
            state = (i, exp)
            if state not in memo:
                memo[state] =  dp(i +1, exp + (-1 *nums[i])) + dp(i+1, exp + nums[i])
            return memo[state]
        
        return dp(0, 0)
        
