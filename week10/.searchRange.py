class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
    
        def binarysearch(self, nums, target, leftBias):
            low = 0
            high = len(nums) - 1
            answer = -1
            while low <= high:
                mid = (low + high)//2 
                
                if nums[mid] ==  target:
                    answer = mid
                    if leftBias :
                        high = mid - 1
                    else:
                        low = mid + 1     
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return answer
        left = binarysearch(self,nums , target , True)
        right = binarysearch(self,nums , target , False)
        return [left , right]
        
        # if start <= end <len(nums) and nums[start]== nums[end] == target:
        #     return [start, end]
        # else:
        #     return [-1, -1]
                
