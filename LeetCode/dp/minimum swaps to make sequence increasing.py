class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        

      
        @cache
        def dp(i, is_swap):
            if i >= len(nums1):
                return 0

            if is_swap:
                prev1 = nums2[i-1]
                prev2 = nums1[i -1]
            else:
                prev1 = nums1[i-1]
                prev2 = nums2[i -1]
         
            if i == 0:
                return min(dp(i + 1, True) + 1, dp(i + 1, False))

            count = inf
        
            if nums1[i] >  prev2 and nums2[i] > prev1:
                count = min(count, dp(i + 1,  True) + 1)
            if nums1[i] > prev1 and nums2[i] > prev2:
                count = min(count, dp(i + 1, False))

            return count        
        
        return dp(0, False)

            
                
            

            


