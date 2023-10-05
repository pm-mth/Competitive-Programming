class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        @cache
        def dp(i, j):
            if i >= len(nums1) or j >= len(nums2):
                return 0

            left = 0
            for k in range(j, len(nums2)):
                if nums2[k] == nums1[i]:
                    left = dp( i + 1, k + 1) + 1
                    break

            right = dp(i + 1, j)
            return max(left, right)
        
        return dp(0, 0)
        
