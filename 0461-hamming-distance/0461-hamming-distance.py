class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        mask = 1
        max_num = max(x, y)
        ans = []
        
        i = 0
        while mask <= max_num:
            if x & mask != y & mask:
                ans.append(i)      
            mask <<= 1
            i += 1

        
        return len(ans)