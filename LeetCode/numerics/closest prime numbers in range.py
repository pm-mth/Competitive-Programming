class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
       
        val = self.generatePrimes(right)
        primes = []
        for i in range(left, right + 1):
            if val[i]:
                primes.append(i)
        if len(primes) < 2:
            return [-1, -1]
        

        min_val = inf #track the minimum difference
        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < min_val:
                min_pairs = [primes[i- 1], primes[i]]
                min_val = min(min_val, primes[i] - primes[i -1])
        return min_pairs

    def generatePrimes(self, n):
        if n < 2:
            return [False, False]

        isPrime = [True for _ in range(n + 1)]
        isPrime[0] = isPrime[1] = False

        i = 2
        while i * i <= n:
            j = i * i 
            while j <= n:
                isPrime[j] = False
                j += i
            if i > 2:
                i += 2
            else:
                i += 1
     
        return isPrime
