class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        m = len(b)
        n = len(a)
        l, r = 0, 1

        LPS = [0] * m
        while r < m:
            if b[r] == b[l]:
                l += 1
                LPS[r] = l
                r += 1
            elif l == 0:
                r += 1
            else:
                l = LPS[l-1]
        
        count = 0
        l, r = 0, 0
        length = n
        found = False
       
        while length <= max(2* m, 2*n):
            if l == n:
                l = 0
                length += n
            
            if r < m  and l < n and b[r] == a[l]:
                l += 1
                r += 1
                if r == m:
                    found = True
                    break

                
            elif r > 0:
                r = LPS[r-1]
            else:
                l += 1
                       
               
        if found:
            return length // n
        
        return -1


        
