class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        countS = defaultdict(int)
        answer = sys.maxsize
        l = 0
        left, right = 0, 0
        window = 0
        for r in range(len(s)):
            if s[r] in t:
                countS[s[r]] += 1
                if countS[s[r]] == countT[s[r]]:
                    window += 1      
                    
            while l <= r and window == len(countT):
                if r - l + 1 < answer:
                    left, right = l, r
                    answer = r - l + 1
                    
                if s[l] in t:
                    countS[s[l]] -= 1
                    if countS[s[l]] < countT[s[l]]:
                        window -= 1
                        
                    if countS[s[l]] == 0:
                        del countS[s[l]]     
                l += 1
        if answer == sys.maxsize:
            return ""
        return s[left:right+1]
            
                    
        