class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        subarray = 0
        
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        for i in range(len(nums)):
            if nums[i] - goal in count:
                subarray += count[nums[i] - goal]
            
            count[nums[i]] += 1
                
        return subarray
        
        
        