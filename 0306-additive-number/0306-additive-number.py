class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) <= 2:
            return False
        self.num = num
        self.answer = False
        self.checkAddition(0, [])
        return self.answer
        
    def checkAddition(self, idx, prev):
        if idx == len(self.num) and len(prev) <= 2:
            return 
        
        if idx == len(self.num):
           
            self.answer = True
            return
        
        cur = ""
        for i in range(idx, len(self.num)):
            cur += self.num[i]
            
            if len(cur) > 1 and cur[0] == "0":
                return
         
            
            if len(prev) < 2 or int(cur) == int(prev[-1]) + int(prev[-2]):
                prev.append(cur)
                self.checkAddition(i + 1, prev)
                prev.pop()
    
            
            if len(prev) >= 2 and   ( int(cur) > int(prev[-1]) + int(prev[-2]) or (int(prev[-1]) + int(prev[-2]) < int(cur))):
                return  
            
           
            
           
            
            
    
            
            
            
            
            
            
        