class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        longest = 0
        for end in range(len(s)):
            if s[end] in seen and seen[s[end]] >= start:
                start = seen[s[end]] + 1
            seen[s[end]] = end
            longest = max(longest, end - start + 1)
        return longest