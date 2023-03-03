class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        running_min = []
        min_ = nums[0]
        for num in nums:
            min_ = min(min_, num)
            running_min.append(min_)
        
        stack = []
        for i in range(len(nums)- 1, -1, -1):
         
            while stack and stack[-1] < nums[i]:
                if stack[-1] > running_min[i] and nums[i] > stack[-1]:
                    return True
                    
                stack.pop()
                    
            stack.append(nums[i])
            
        return False
            
                
                
            
        