class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        overlap = 0
        n = len(img1)

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < n

        

        @cache
        def dp(l ,up):
            if abs(l) > n or abs(up) > n:
                return 0
                
        
            count = 0
            for i in range(n):
                for j in range(n):
                    r = i + l
                    c = j + up
                    if inbound(r, c):
                        if img1[r][c] == img2[i][j] == 1:
                            count  += 1

            if l == 0:
                count = max(dp(l+1, up), dp(l-1, up), count)
            if up == 0:
                count = max(dp(l, up+ 1), dp(l, up-1), count)

            if l > 0:
                if up >= 0:
                    return max(dp(l + 1, up), dp(l, up + 1) , count)
                else:
                    return max(dp(l + 1, up), dp(l, up - 1), count)

            if l < 0:
                if up >= 0:
                    return max(dp(l - 1, up),  dp(l, up + 1), count)
                else:
                    return max(dp(l - 1, up), dp(l, up - 1), count)

           
            
            return count
            
        
        count = 0
        for i in range(n):
            for j in range(n):
                if img1[i][j] == img2[i][j] == 1:
                    count += 1
        
        return dp(0, 0)

               
        
        

            



            
            
