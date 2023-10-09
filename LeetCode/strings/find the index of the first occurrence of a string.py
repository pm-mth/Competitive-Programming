class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        LPS = [0] * len(needle)
        l, r = 0, 1
        while r < len(needle):
            if needle[r] == needle[l]:
                LPS[r] = l + 1
                l += 1
                r += 1
            elif l == 0:
                r += 1
            else:
                l = LPS[l - 1]
        
        l, r = 0, 0
        while r < len(haystack):
            if haystack[r] == needle[l]:
                l += 1
                r += 1
            elif l == 0:
                r += 1
            else:
                l = LPS[l-1]
        
            if l == len(needle):
                return r - len(needle)
               
        return -1
            
        
