class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative = []
        positive = []
        
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
        modified_array = []
        for i in range(len(positive)):
            modified_array.append(positive[i])
            modified_array.append(negative[i])
            
        return modified_array
            
        