class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0] * (len(nums) + 1)
        
        for req in requests:
            prefix[req[0]] += 1
            prefix[req[1] + 1] += -1
            
        for r in range(1, len(nums) + 1):
            prefix[r] = prefix[r-1] + prefix[r]
        
        prefix.sort(reverse = True)
        nums.sort(reverse = True)
        
        max_total_sum = 0
        for r in range(len(nums)):
            max_total_sum += prefix[r] * nums[r]
        
        return max_total_sum % (10**9 + 7)
            
            
            
            