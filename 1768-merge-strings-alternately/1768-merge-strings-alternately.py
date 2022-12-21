class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        n = len(word1)
        m = len(word2)
        for i in range(n):
            ans += word1[i]
            if i < m:
                ans += word2[i]
        if m > n:
            ans += word2[n:m]
        return ans