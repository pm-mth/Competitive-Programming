class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        size = len(s1)
        window_count = Counter()
        l = 0
        for r in range(len(s2)):
            window_count[s2[r]] += 1
            if size == r - l + 1:
                if s1_count == window_count:
                    return True
                else:
                    window_count[s2[l]] -= 1
                    if  window_count[s2[l]] == 0:
                        del window_count[s2[l]]  
                    l += 1    
        return False
            
        