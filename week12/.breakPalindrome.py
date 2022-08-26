class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        for i in range(n):
            if palindrome[i] != "a":
                local = palindrome[:i] + 'a' + palindrome[i + 1:]
                reverse = local[:n//2 -1:-1]
                if n%2 == 0:
                    end = n//2
                else:
                    end = n//2 +1
                if local[:end] != reverse:
                    return local
                
        return palindrome[:n-1] + 'b'
        
