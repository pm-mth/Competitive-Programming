class Solution:
    def longestPrefix(self, s: str) -> str:

        l, r = 0, 1
        n = len(s)
        LPS = [0] * n
       
        while r < n:
            if s[l] == s[r]:
                l += 1
                LPS[r] = l
                r += 1
            elif l == 0:
                r += 1
            else:
                l = LPS[l - 1]
  
       
        res =  ""
       
        for i in range(LPS[-1]):
            res += s[i]
        
        return res
        
        
                
        
