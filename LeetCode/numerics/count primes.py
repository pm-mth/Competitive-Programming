class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [True for _ in range(n)]
        is_prime[0] = is_prime[1] = False
        
        i = 2
        while i * i < n:
            while i*i <  n and is_prime[i] == False:
                i += 2

            j = i * i
            while j < n:
                is_prime[j] = False
                j += i
            if i > 2:
                i += 2
            else:
                i += 1
        
        return is_prime.count(True)     
                
            
        
