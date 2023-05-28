class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = defaultdict(int)
        n = len(cost)

        def solve(n):
            if n <= 1:
                return cost[n]
            if dp[n]:
                return dp[n]
            oneStep = solve(n - 1)
            twoStep = solve(n -2)
    
            dp[n] = min(oneStep, twoStep) + cost[n]


            return dp[n] 
        oneStep = solve(n -1)
        twoStep = solve(n - 2)
        

        return min(oneStep, twoStep)
