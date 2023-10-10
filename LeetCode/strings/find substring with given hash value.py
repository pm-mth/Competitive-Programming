class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:

        s = s[::-1]
        offset = ord('a') - 1
        hash_key = 0

       
        for r in range(k):
            idx = ord(s[r]) - offset
            hash_key += pow(idx * pow(power,  k - r - 1, modulo), 1, modulo)
            hash_key %= modulo
        

       
        if hash_key == hashValue:
            index = 0

        
        for r in range(k, len(s)):
            idx = ord(s[r - k]) - offset
            hash_key -= pow(idx * pow(power, k - 1, modulo), 1, modulo)
            
            hash_key = ((hash_key) * (power % modulo) +  (ord(s[r]) - offset) ) % modulo
            if hash_key == hashValue:
                index = r - k + 1
        
        return s[index: index + k][::-1]




        
