class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        mask = 1
        max_num = max(x, y)
        ans = 0
        while mask <= max_num:
            if x & mask != y & mask:
                ans += 1
            mask <<= 1
        
        return ans