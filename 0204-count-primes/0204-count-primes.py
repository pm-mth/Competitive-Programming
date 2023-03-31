class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [True for _ in range(n)]
        is_prime[0] = is_prime[1] = False
        
        i = 2
        while i * i < n:
            j = i * i
            while j < n:
                is_prime[j] = False
                j += i
            if i > 2:
                i += 2
            else:
                i += 1
        count = 0
        for i in range(len(is_prime)):
            if is_prime[i] == True:
                count += 1
        return count       
                
            
        