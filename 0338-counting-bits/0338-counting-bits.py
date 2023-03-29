class Solution:
    def countBits(self, n: int) -> List[int]:
        bitCounts = []
        for i in range(n + 1):
            count = 0
            while i > 0:
                if i&1:
                    count += 1
                i >>= 1
            bitCounts.append(count)
        return bitCounts