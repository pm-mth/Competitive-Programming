class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] += 1
        total_subarray = 0
        if nums[0] - k in prefix_count:
                total_subarray += prefix_count[nums[0] - k]
        prefix_count[nums[0]] += 1
                
        for r in range(1, len(nums)):
            nums[r] = nums[r-1] + nums[r]
            
            if nums[r] - k in prefix_count:
                total_subarray += prefix_count[nums[r] - k]
            prefix_count[nums[r]] += 1
            
        return total_subarray
                
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         for r in range(1, len(nums)):
#             nums[r] = nums[r-1] + nums[r]
    
#         l = 0
#         accumulator, count = 0, 0
#         for r in range(len(nums)):
#             accumulator = nums[r]
#             loop = False
#             while l <= r and accumulator > k:
#                 if l > 0 and loop == True:
#                     accumulator -= nums[l] - nums[l-1]
#                 else:
#                     accumulator -= nums[l]
#                 l += 1
#                 loop = True
#             if accumulator == k:
#                 count += 1
            
#         return count
            
                
            
        