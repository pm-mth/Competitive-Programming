class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs) ): 
            ans = ""
            for j in range(len(prefix)):
                
                if j < len(strs[i]) and prefix[j] == strs[i][j]:
                    ans += prefix[j]
                else:
                    break
            prefix = ans
        return prefix
                    
                    
            
        