class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        candidates = []  
        nums.sort()
    
        def findSubsets(ind, inter):
            if ind == len(nums):
                candidates.append(deepcopy(inter))
                return 
           
            inter.append(nums[ind])
            findSubsets(ind + 1, inter)
            
            while ind + 1 < len(nums):
                if nums[ind] == nums[ind + 1]:
                    ind += 1
                else:
                    break
                    
            inter.pop()
            findSubsets(ind + 1, inter)
        
        findSubsets(0, [])
        
        return candidates
        