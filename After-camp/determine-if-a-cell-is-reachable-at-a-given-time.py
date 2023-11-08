class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x = abs(fx  -sx)
        y = abs(fy -sy)

        if not x and not y and t == 1:
            return False
            

        if t < max(x, y):
            return False
        
        return True