class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:


        @cache
        def dp(add, i):
            if i == len(stones):
                return add
            
            pos = dp(add + stones[i], i + 1)
            neg = dp(add - stones[i], i + 1)
    
            if pos >= 0 and neg >= 0:
                return min(pos, neg)
            
            if pos >= 0:
                return pos
            if neg >= 0:
                return neg
            
            return -100
        
        return dp(0, 0)
        

        
