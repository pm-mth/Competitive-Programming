class Solution:
    def __init__(self):
        self.root = [None, None]

    def insert(self, key: str) -> None:
        cur = self.root
        for ch in key:
            if not cur[int(ch)]:
                cur[int(ch)] = [None, None]
            cur = cur[int(ch)]
      
    
    
    def dfs(self, left, right):
        if not left[0] and not left[1]:
            return ("", "")
    

        l, r = 0, 0
        b1, s1, b2, s2 = "", "", "", ""
        if left[0] and right[1] or left[1] and right[0]:
            if left[0] and right[1]:
                b1, s1 = self.dfs(left[0], right[1])
                if b1:
                    l = int(b1, 2) ^ int(s1, 2)
            if left[1] and right[0]:
                b2, s2 = self.dfs(left[1], right[0])
                if b2:
                    r = int(b2, 2) ^ int(s2, 2) 
        else:
            if left[0] and right[0]:
                b, s = self.dfs(left[0], right[0])
                return ("0" + b, "0" + s)
                
            elif left[1] and right[1]:
                b, s = self.dfs(left[1], right[1])
                return ("1" + b, "1" + s)
        
        if l > r:
            return ("0" + b1, "1" + s1)
        elif r > l:
            return ("1" + b2, "0" + s2)
        else:
            if b1:
                return ("0" + b1, "1" + s1)
            else:
                return ("1" + b2, "0" + s2)


    def findMaximumXOR(self, nums: List[int]) -> int:
        great =  max(nums)
        for num in nums:
             mask = 1
             bits = ""
             if great == 0:
                 bits = "0"
             while mask <= great:
                 bit = mask & num 
                 if bit:
                    bits = "1" + bits
                 else:
                     bits = "0" + bits
                 mask <<= 1

          
             self.insert(bits)
        
        cur = self.root
        
        l, r = 0, 0
        if cur[0] and cur[1]:
            l, r = self.dfs(cur[0], cur[1])
            l = "0" + l 
            r = "1" + r
            
        elif cur[0]:
            l, r = self.dfs(cur[0], cur[0])
            l = "0" + l
            r = "0" + r
        else:
            l, r = self.dfs(cur[1], cur[1])
            l  = "1" + l
            r = "1" + r
        
        return int(l, 2) ^ int(r, 2)
                 
