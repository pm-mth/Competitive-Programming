class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        goal = n -1
        start = goal - 1
        while start >= 0:
            if nums[start] >= goal - start:
                goal = start
                start -= 1
            else:
                start -= 1
        return goal == 0 
            
        
