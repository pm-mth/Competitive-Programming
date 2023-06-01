class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        answer = [inf] *(amount + 1)
        answer[0] = 0
        coins.sort()
        for am in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] > am:
                    break
                answer[am] = min(answer[am - coins[j]] + 1, answer[am])
            
        if answer[amount] == inf:
            return -1
    
        return answer[amount] 
        
        
        
        
