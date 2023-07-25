class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = defaultdict(int)
        n = len(prices)
        
        def solve(i, buying):
            if i >= n:
                return 0
            if cache[(i, buying)]:
                return cache[(i, buying)]
            if buying:
                buy = solve(i+1, not buying) - prices[i]
                coolDown = solve(i+1, buying)
                cache[(i, buying)] = max(buy, coolDown)
            else:
                sell = solve(i+2, not buying) + prices[i]
                coolDown = solve(i+1, buying)
                cache[(i, buying)] = max(sell, coolDown)
            return cache[(i, buying)]
        
        return solve(0, True)
            
            
