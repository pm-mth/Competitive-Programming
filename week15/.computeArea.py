class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        
        aArea = (ax2 - ax1) * (ay2- ay1)
        bArea = (bx2 - bx1) * (by2- by1)
        intersect = (min(bx2,ax2) - max(bx1, ax1)) * (min(by2, ay2) - max(by1, ay1))
        
        if (bx1 >= ax2 ) or (ax1 >= bx2):
            return aArea + bArea 
        elif (by1 >= ay2) or (ay1 >= by2): 
            return aArea + bArea   
        else:
            return aArea + bArea - intersect
            
