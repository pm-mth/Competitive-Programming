class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
       
        newNums= []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i] and j != i:
                    count += 1
            newNums.append(count)
            
        return newNums
                
