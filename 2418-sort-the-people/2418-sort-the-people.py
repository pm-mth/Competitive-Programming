class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
      
        #bubble Sort
        
#         index = 0
#         while index < len(names):
#             swap = 0
#             for j in range(index, len(heights)-1):
#                 if heights[j] < heights[j+1]:
#                     heights[j], heights[j+1] = heights[j+1], heights[j]
#                     names[j],  names[j+1] = names[j+1], names[j]
#                     swap += 1
#             if swap == 0:
#                 index = len(names)
            
#             index += 1
#         return names
        
    #selection Sort
    
        for i in range(len(names)):
            curMin = i
            for j in range(i, len(names)):
                if heights[curMin] < heights[j]:
                    curMin = j
            heights[curMin], heights[i] = heights[i], heights[curMin]
            names[curMin], names[i] = names[i], names[curMin]
            
        return names