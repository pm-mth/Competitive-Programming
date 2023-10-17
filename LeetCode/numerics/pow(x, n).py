class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n > 1:
            if n % 2 == 0:
                return self.myPow(x, n // 2) * self.myPow(x, n//2)
            elif n % 2 != 0:
                return self.myPow(x, n // 2) * self.myPow(x, n//2) * x
        else:
            return 1/self.myPow(x, -1*n)
        

        
