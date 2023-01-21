class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        arr_length = len(nums)
        
        for i in range(arr_length):
            string_num = str(nums[i])
            if len(string_num) == 1:
                nums.append(nums[i])
            else:
                string_num = string_num[::-1]
                nums.append(int(string_num))
        distinct_int = set(nums)
        return len(distinct_int)
            
        