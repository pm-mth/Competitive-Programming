class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        candidates = []
    
        def findSubsets(ind, inter):
            if ind == len(nums):
                candidates.append(deepcopy(inter))
                return 
            
            inter.append(nums[ind])
            findSubsets(ind + 1, inter)
            inter.pop()
            findSubsets(ind + 1, inter)
        
        findSubsets(0, [])
        
        return candidates
            
        
        
        
        
        
        
        