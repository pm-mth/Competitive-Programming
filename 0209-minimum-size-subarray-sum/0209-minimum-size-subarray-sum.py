class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = sys.maxsize
        l = 0
        curSum = 0
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                minLen = min(minLen, r - l + 1)
                curSum -= nums[l]
                l += 1
        
        if minLen != sys.maxsize:
            return minLen
        else:
            return 0
            