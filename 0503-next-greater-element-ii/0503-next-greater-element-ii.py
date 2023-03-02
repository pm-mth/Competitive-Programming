class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        greater_number = [-1] * len(nums)
        stack = []
        
        for r in range(2*len(nums)):
            r = r % len(nums)
            while stack and nums[stack[-1]] < nums[r]:
                greater_number[stack[-1]] = nums[r]
                stack.pop()
            
            stack.append(r)
        
        return greater_number
                
        
        