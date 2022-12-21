class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        l, r = 0, 2
        while r < len(nums):
            if nums[l] + nums[l +1] >nums[r] and nums[l +1] + nums[r] > nums[l] and nums[l] + nums[r] > nums[l + 1]:
                ans = max(ans, nums[l] + nums[l+1]+ nums[r])
                l += 1
                r += 1
            else:
                l += 1
                r += 1
        return ans