class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort(reverse = True)
        last = 2*(len(piles) // 3)
        answer = 0
        
        for i in range(1, last, 2):
            answer += piles[i]
            
        return answer
            
        
