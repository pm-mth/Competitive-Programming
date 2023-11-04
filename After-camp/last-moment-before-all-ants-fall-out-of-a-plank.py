class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        l = 0
        r = n

        if left:
            l = max(left)
        if right:
            r = min(right)

        
        return max(l,n - r)