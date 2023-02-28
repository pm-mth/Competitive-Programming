class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        letters = [0] * (len(s)+1)
       
        for shift in shifts:
            if shift[2] == 0:
                letters[shift[0]] -= 1
                letters[shift[1]+1] += 1
            else:
                letters[shift[1]+1] -= 1
                letters[shift[0]] += 1
        
        
        accumulator = 0
        shifted_ch = []
        for i in range(len(s)):
            accumulator += letters[i]
            ch = (ord(s[i]) - ord("a") + accumulator)%26
            shifted_ch.append(chr(ch + ord('a')))
        return "".join(shifted_ch)
            
  
                    
                
                
            
        