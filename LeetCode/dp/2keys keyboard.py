class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        # res = inf
       
        @cache
        def solve(i, op):
            # print(i, op)
           
            if i  == n:
                return 1
            if i >= n:
                return n
            if op != i:
                return min(solve(i + op, op), solve(i, i )) + 1
            
            return solve(i + op, op) + 1
        
        
        return solve(1, 1)
        
    


                
