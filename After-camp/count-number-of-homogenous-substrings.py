class Solution:
    def countHomogenous(self, s: str) -> int:
        s += "Z"
        l, res = 0, 0
        for r in range(len(s)):
            if s[r] != s[l]:
                dp = ((r - l)*(r - l + 1))//2
                res += dp
                l = r

        return res % (10**9 + 7)
            


       