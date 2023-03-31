class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        flag = n & 1
        mask = 1
        while mask < n:
            mask <<= 1
            ans = n & mask
            if ans and flag or not (ans or flag):
                return False
            flag = ans
        return True
                
        
        