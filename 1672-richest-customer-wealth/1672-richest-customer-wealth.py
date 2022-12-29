class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for i in range(len(accounts)):
            wealth = 0
            for j in range(len(accounts[0])):
                wealth += accounts[i][j]
            ans = max(ans, wealth)
        
        return ans
        