class Solution:
    def countArrangement(self, n: int) -> int:
        self.answer = 0
        self.n = n
        used = 0
        self.findPermutation(1, [], used)

        return self.answer
    

    def findPermutation(self, i, inter, used):
        if len(inter) == self.n :
            self.answer += 1
            return 
        
        for j in range(1, self.n + 1):
            if not (i % j == 0 or j % i == 0):
                continue
            if used & 1 << j - 1:
                continue
            used |= 1 << j - 1
            inter.append(j)
            self.findPermutation(i+1, inter, used)
            used ^= 1 << j - 1
            inter.pop()

        return
        
    
    
