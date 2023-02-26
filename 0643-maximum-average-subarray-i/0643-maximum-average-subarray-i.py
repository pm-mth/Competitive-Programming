class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = float(-inf)
        curSum = 0
        left = 0
        for right in range(len(nums)):
            if right - left + 1 > k:
                avg = curSum / k
                maxAvg = max(maxAvg, avg)
                curSum -= nums[left]
                left += 1
            curSum += nums[right]
        avg = curSum / k
        maxAvg = max(maxAvg, avg)
        return maxAvg
        