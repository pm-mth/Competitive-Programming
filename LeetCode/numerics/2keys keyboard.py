class Solution:
    def minSteps(self, n: int) -> int:
        primes = []

        d = 2
        while d * d <= n:
            while n % d == 0:
                primes.append(d)
                n //= d
            d += 1
        if n > 1:
            primes.append(n)
        print(primes)   
        return sum(primes)


        
