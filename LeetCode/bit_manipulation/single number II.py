class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        for i in range(len(nums)):
            nums[i] -= 2**31

        i = 0
        answer = 0
        while  i < 32:
            mask = 1 << i
            count = 0
            for num in nums:
                count += num & mask
            res = count % 3
            if res:
                answer |= mask
            i += 1
        answer -= 2**31
        
            
        return answer
        
