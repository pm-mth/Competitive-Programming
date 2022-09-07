class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        profit = 0
        for i in range(len(prices)):
            if stack and stack[-1] > prices[i]:
                stack.pop()
                stack.append(prices[i])
            elif stack and stack[-1] <= prices[i]:
                profit = max(profit, prices[i] - stack[-1])
            else:
                stack.append(prices[i])
        return profit
        
        
        
