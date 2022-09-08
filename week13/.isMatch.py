class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #Top-down memoization
        
        n, m = len(s), len(p)
        cache = {}
        def regExpression(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if j >= m and i >= n:
                return True
            if j >= m:
                return False
            match = i < n and (s[i] == p[j] or p[j] == ".")
            if j+1 < m and p[j+1] == "*":
                cache[(i,j)] =((match and regExpression(i+1, j)) #use
                                or regExpression(i,j+2) )  # don't use
                return cache[(i,j)]
            
            if match:
                cache[(i,j)] = regExpression(i+1, j+1)
                return cache[(i,j)]
            cache[(i,j)] = False    
            return False
        
        return regExpression(0, 0)    
        
