class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if k == 1:
            return 0
       
        
        
        mid = 2 **(n -2)
        
        if k <= mid:
            return self.kthGrammar(n - 1, k)
        else:
            if self.kthGrammar(n - 1, k - mid):
                return 0
            else:
                return 1
           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def find (count, n, k, s):
#             if count == n:
#                 return int(s[k - 1])
            
#             newString = ""
#             for i in range(len(s)):
#                 if s[i] == "0":
#                     newString += "01"
#                 else:
#                     newString += "10"
                
#             print(newString)
#             return find(count + 1, n, k, newString )
        
#         return find(1, n, k, "0")
        