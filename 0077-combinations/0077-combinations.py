class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        candidates = []
        
        def findCombinations(ind, k , inter):
            if k == 0:
                candidates.append(deepcopy(inter))
                return
            
            if ind > n:
                return 
            
            
            inter.append(ind)
            findCombinations(ind + 1, k - 1, inter)
            inter.pop()
            findCombinations(ind + 1, k, inter)
        
        findCombinations(1, k, [])
        
        return candidates
            
        
        