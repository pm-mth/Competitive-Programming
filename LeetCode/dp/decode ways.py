class Solution:
    def numDecodings(self, s: str) -> int:
        dp = defaultdict(int)

        def dfs(i, left):
            if i >= len(s):
                return 1
                
            if dp[i]:
                return dp[i]
                
            temp = ""
            for j in range(len(left)):
                temp += left[j]
                if temp[0] == "0":
                    return 0

                if int(temp) > 26:
                    return dp[i]

                dp[i] += dfs(i + j + 1,  left[j + 1:])
    
            return dp[i]
            
        return dfs(0, s)
            


                    
        
