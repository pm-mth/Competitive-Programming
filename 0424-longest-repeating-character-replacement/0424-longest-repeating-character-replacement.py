class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        longest = 0
        maxfreq = 0
        
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxfreq = max(maxfreq, count[s[r]])
            
            if (r - l + 1) - maxfreq > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l +1)
        return longest
                
                