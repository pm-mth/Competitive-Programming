class Solution:
    def splitString(self, s: str) -> bool:
        self.s = s
        self.answer = False
        self.findPaths(0, [])
        return self.answer
        
    
    def findPaths(self, idx, prev):
        if prev and len(self.s) == len(prev[-1]):
            return
        
        if idx == len(self.s):
            self.answer = True
            return 
        
        cur = ""
        for i in range(idx, len(self.s)):
            cur += self.s[i]
        
            if not prev or int(prev[-1]) - int(cur) ==1:
                prev.append(cur)
                self.findPaths(i + 1, prev)
                prev.pop()
                
            if prev and int(cur) > int(prev[-1]):
                return
        
        
        
        
        
        
        
       
        
      
        
        
        
        
        
           
            
            
            