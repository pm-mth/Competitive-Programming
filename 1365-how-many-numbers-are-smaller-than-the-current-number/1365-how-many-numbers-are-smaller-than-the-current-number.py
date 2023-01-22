class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        num_index = []
        for i in range(len(nums)):
            num_index.append((nums[i], i))
        num_index.sort()
        
        
        for i in range(len(num_index)):
            if i > 0 and num_index[i][0] == num_index[i-1][0]:
                nums[num_index[i][1]] = index
            else:
                index = i
                nums[num_index[i][1]] = index 
        return nums
        