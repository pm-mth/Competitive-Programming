class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        #map into dictionary of indexs
        index = defaultdict(int)
        for i in range(len(nums)):
            index[nums[i]] = i
        
        #do the operations
        for i in range(len(operations)):
            indx = index.pop(operations[i][0])
            index[operations[i][1]] = indx
           
       #sort the elements by the second elements
        nums = sorted(index.items(), key=lambda x:x[1]) 

        
        #return the first element
        return [nums[i][0] for i in range(len(nums))]
        