class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def solve(x, n):
            if n == 1:
                return x
            if n == 0:
                return 1
            
            
            if n%2 != 0:
                carry = x
            else:
                carry = 0
            
            res = solve(x, n//2)
            
            if carry:
                return res * res *carry
            else:
                return res * res
        
        if n < 0:
            ans = solve(x, -1*n)
            return 1/ans
        else:
            return solve(x, n)
        
            
            
            
        
        