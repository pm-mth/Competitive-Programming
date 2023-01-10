class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        pivot = num//3
        candidates = [pivot-1,pivot,pivot+1]
        
        for candidate in candidates:
            total = candidate*3+3
            if total == num:
                return [candidate,candidate+1,candidate+2]
        
        return []
        
            
        
        