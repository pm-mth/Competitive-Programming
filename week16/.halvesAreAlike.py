class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        Act =0
        Bct =0
        for i in range(len(s)):
            if i < n//2 and s[i] in vowel:
                Act += 1
            elif i >= n//2 and s[i] in vowel:
                Bct += 1
            
        if Act == Bct:
            return True
        return False     
        # n = len(s)
        # a = s[:n//2]
        # b = s[n//2:]
        # Act =0
        # for i in range(len(a)):
        #     if a[i] in vowel:
        #         Act += 1
        # Bct =0
        # for i in range(len(b)):
        #     if b[i] in vowel:
        #         Bct += 1
        
