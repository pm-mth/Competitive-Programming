class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        array = []
        nums.sort()
        mid = len(nums)//2
        i = 0
        j = mid +1
        while i <= mid and j < len(nums):
            array.append(nums[i])
            array.append(nums[j])
            i += 1
            j += 1
        
        while i <= mid:
            array.append(nums[i])
            i += 1
        
        while j < len(nums):
            array.append(nums[j])
        
            
        
#         for i in range(len(nums)):
#             for j in range(1, len(nums)-1):
#                 if (nums[j-1] + nums[j+1])/2 != nums[j]:
#                     nums[j-1], nums[j] =  nums[j-1], nums[j]
#                 else:
#                     nums[j], nums[j+1] = nums[j+1], nums[j]
                    
        
        return array        
                
