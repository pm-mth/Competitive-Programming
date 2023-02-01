class Solution:
    def partitionLabels(self, s: str) -> List[int]:
    
        
        endPlace = defaultdict(int)
        for i in range(len(s)):
            endPlace[s[i]] = i
              
        result = []    
        position = 0
        total = 0
        for i in range(len(s)):
            position = max(position, endPlace[s[i]])
            if i == position:
                result.append(position + 1 - total)
                total = position + 1

        return result
                
        