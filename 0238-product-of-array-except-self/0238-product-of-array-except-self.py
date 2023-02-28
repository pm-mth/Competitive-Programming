class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [1]*n, [1]*n
        product_arr = []
        
        for r in range(1,n):
            left[r] = left[r-1] * nums[r-1]
        
        reversed_nums = nums[::-1]
        for r in range(1, n):
            right[r] = right[r-1] * reversed_nums[r-1]
        
        reversed_right = right[::-1]
        for r in range(n):
            product_arr.append(reversed_right[r] * left[r])
        
        return product_arr
    
            
        
            
            
            
        