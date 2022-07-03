class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=list(map(str, nums))
        result = ""
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        
        result =''.join(nums)   
        
        if result == "0"*len(result):
            return "0"
        else:
            return result
                
                
            
            
        
#         **nums.sort(reverse= True, key = lambda x : nums[1])
       
#         newlist= [char for char in nums]
#         nums = list(map(int, newlist))
#         nums.sort(reverse=True)
#         nums = list(map(str, nums))               
#         nums=''.join(nums)    
       
        
            
        
