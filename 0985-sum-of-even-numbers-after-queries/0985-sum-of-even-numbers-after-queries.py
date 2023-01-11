class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        # find the intial sum of even numbers
        sum_even = 0
        for num in nums:
            if num%2 == 0:
                sum_even += num
                
        #for each given queries it find th e sum of even values
        final_answer = []
        for i in range(len(queries)):
        
            if nums[queries[i][1]]%2 == 0:
                sum_even -= nums[queries[i][1]]
            
            #do the given operation in each queries    
            operation = nums[queries[i][1]] + queries[i][0]
            nums[queries[i][1]] = operation
            
    
            if operation%2 == 0:
                sum_even += operation
                
            #append the even values at a given index   
            final_answer.append(sum_even)
        return final_answer
            