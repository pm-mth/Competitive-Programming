"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        
        answer = []
        for x in range(1, z + 1):
            low, high = 0, z
            
            while high > low + 1:
                mid  = (low + high)//2
                if customfunction.f(x, mid) >= z:
                    high = mid
                else:
                    low = mid 
            if customfunction.f(x, high) == z:
                answer.append([x, high])
            
        return answer
        
        
