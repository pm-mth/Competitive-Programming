class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxval, minval = max(nums), min(nums)
        
        count = [0] * (maxval - minval + 1)
        for i in range(len(nums)):
            offset = nums[i] - minval
            count[offset] += 1
          
        acc = 0
        for i in range(len(count) - 1, -1, -1):
            acc += count[i]
            if acc >= k:
                return  minval + i
            
        
        
        