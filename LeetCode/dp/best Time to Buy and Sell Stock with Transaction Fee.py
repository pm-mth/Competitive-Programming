class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        
        def dfs(index, decide):
            if index >= len(prices):
                return 0
            
            if (index, decide) in memo:
                return memo[(index, decide)]
            
            if decide:
                buy = dfs(index + 1, not decide) - prices[index]
                not_buy = dfs(index + 1, decide)
                memo[(index, decide)] = max(buy, not_buy)
            
            else:
                sell = dfs(index + 1, not decide) + prices[index] - fee
                not_sell = dfs(index +1, decide)
                memo[(index, decide)] = max(sell, not_sell)
            
            return memo[(index, decide)]
        return dfs(0, True)
