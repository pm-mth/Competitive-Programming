class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        count2 = defaultdict(int)
    

        l, r = 0, 0
        while r < len(s2):
            if r >= len(s1):
                count2[s2[l]] -= 1
                if not count2[s2[l]]:
                    del count2[s2[l]]  
                l += 1          
           

            count2[s2[r]] += 1
            if count1 == count2:
                return True
            r += 1
        return False
            
        
