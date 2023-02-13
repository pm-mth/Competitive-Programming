class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        def rotate (arr, l, r):
            while l < r and r < len(nums):
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        if k > len(nums):
            k = k % len(nums) 
                
        rotate(nums, 0, len(nums)-1)
        rotate(nums, 0, k-1)
        rotate(nums, k, len(nums)-1)
        
        
        