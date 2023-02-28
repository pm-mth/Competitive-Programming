class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        array_count = defaultdict(int)
        array_count[0] += 1
        prefix = [0]*len(nums)
        nice_subarray = 0
        
        #intialize the first element 
        if nums[0]%2 != 0:
            prefix[0] = 1
        array_count[prefix[0]] += 1
        if prefix[0] - k in array_count:
            nice_subarray += array_count[prefix[0]-k]
            
        #finding the prefix sum and subarray
        for i in range(1, len(nums)):
            if nums[i]%2 == 0:
                prefix[i] = prefix[i - 1] + 0
            else:
                prefix[i] = prefix[i - 1] + 1
            
            if prefix[i] - k in array_count:
                nice_subarray += array_count[prefix[i]-k]
            array_count[prefix[i]] += 1
            
            
        return nice_subarray
            
            
                
        
                                              