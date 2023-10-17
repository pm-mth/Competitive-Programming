class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maximum, minimum = max(nums), min(nums)
        diff = maximum - minimum - 2*k
        if diff <= 0:
            return 0
        return diff 
