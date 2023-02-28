class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        subarrays = 0
        count[0] += 1
        
        if nums[0] % k in count:
            subarrays += count[nums[0]% k]    
        count[nums[0]%k] += 1
        
        for r in range(1, len(nums)):
            nums[r] = nums[r] + nums[r-1]
            
            if nums[r] % k in count:
                subarrays += count[nums[r] % k]
            count[nums[r] % k] += 1
    
        return subarrays
       