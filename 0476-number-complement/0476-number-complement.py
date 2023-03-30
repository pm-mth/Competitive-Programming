class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        ans = num

        while mask <= num:
            ans ^= mask
            mask <<= 1
          
        return ans
        