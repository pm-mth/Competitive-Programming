class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        target  = len(cost)
        dp = defaultdict(int)
        
        def dfs(target):
            if target == 1 or target == 0:
                return cost[target]
            if dp[target]:
                return dp[target] 
            first = dfs(target -1)
            second = dfs(target -2)
            dp[target] = cost[target] + min(first, second)
            return cost[target] + min(first, second)
        return min(dfs(target -1), dfs(target -2))
        
