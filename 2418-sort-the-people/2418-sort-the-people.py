class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        index = 0
        while index < len(names):
            swap = 0
            for j in range(len(heights)-1):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j],  names[j+1] = names[j+1], names[j]
                    swap += 1
            if swap == 0:
                index = len(names)
            
            index += 1
        return names
                    
            
        