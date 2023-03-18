class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        if self.isBalanced(count, len(s)//4):
            return 0
        
        left = 0
        minLen = float("inf")
        strings = Counter()
        for right in range(len(s)):
            strings[s[right]] += 1
            
            while left <= right and self.isBalanced(count - strings, len(s)//4):
                minLen = min(minLen, right - left + 1)
                strings[s[left]] -= 1
                left += 1
        
        return minLen     
        
        
    def isBalanced(self, counter, balanced):
        for val in counter.values():
            if val > balanced:
                return False
            
        return True
        
        
        