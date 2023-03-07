class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        ans = [0]*2
      #ending position
        
        left, right = -1, len(nums)
        
        while right > left + 1:
            mid = left + (right - left)//2
            
            if nums[mid] > target:
                right = mid
            else:
                left = mid
        
        ans[1] = left
        
        #starting position
    
        left, right = -1, len(nums)
        
        while right > left + 1:
            mid = left + (right - left)//2
            
            if nums[mid] >= target:
                right = mid
            elif nums[mid] < target:
                left = mid
                
        ans[0] = right
        
        
        #check if the element exist in the array or not
        if ans[0] > ans[1]:
            return [-1, -1]
        else:
            return ans
        
                
                
                    
        
        
            
        
        