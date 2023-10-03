class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        @cache
        def dp(i, l, r):
            if i >= len(costs):
                return 0
            
            left, right = inf, inf

            if l:
                left = dp(i + 1, l-1, r) + costs[i][0]
            if r:
                right = dp(i+1, l, r-1) + costs[i][1]
            return min(left, right)
        
        return dp(0, len(costs)//2, len(costs)//2)
        
