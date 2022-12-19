class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        nw = ""
        for i in range (len(s)):
            if s[i].isalnum():
                nw += s[i]
        return nw == nw[:: -1]