class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        result = ""
        
        # nums = [char for char in num]
        # nums = list(map(int, nums))
        stack = []
        for char in num:
            while stack and k > 0 and stack[-1] > char:
                stack.pop()
                k -= 1
            
            stack.append(char)
      
            
        while k > 0 and stack:
            stack.pop()
            k -= 1
       
        count = 0    
        N = len(stack) 
        for i in range(N):
            if stack[0] == "0":
                del stack[0]
                count += 1
                # str(int(stack))
            else:
                result += stack[i-count]
                
        if result == "":
            return "0"
        else:
            return result
            
        
