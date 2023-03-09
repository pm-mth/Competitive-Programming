class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        child = [0] * k
        
        n = len(cookies)
        res = float('inf')
        
        def findOptimal(i, child):
            nonlocal res            
            if i >= n:
                _max = max(child)
                res = min(_max,res)
                return
            if max(child) >= res:
                return            
            for j in range(k):
                if child[j] + cookies[i] < res:
                    child[j] += cookies[i]
                    findOptimal(i + 1, child)
                    child[j] -= cookies[i]

        cookies.sort(reverse = True)
        findOptimal(0, child)
        return res
        