class Solution:
    def addBinary(self, a: str, b: str) -> str:
        new_a = a[::-1]
        new_b = b[::-1]
        overflow = 0
        ans = []
        i = 0
        while i < len(new_a) and i < len(new_b):
            s1, s2 = int(new_a[i]), int(new_b[i])
            temp = s1 ^ s2 ^ overflow
            ans.append(str(temp))
            if s1 & s2: 
                overflow = 1
            elif s1 | s2 == 0:
                overflow = 0
            i += 1    
            
        while i < len(new_a):
            s1 = int(new_a[i])
            temp = s1 ^ overflow
            if s1 & overflow:
                overflow = 1
            elif s1 | overflow:
                overflow = 0
            ans.append(str(temp))
            i += 1
            
        while i < len(new_b):
            s1 = int(new_b[i])
            temp = s1 ^ overflow
            ans.append(str(temp))
            if s1 & overflow:
                overflow = 1
            elif s1 | overflow:
                overflow = 0
            i += 1
        if overflow:
            ans.append(str(overflow))
        return "".join(ans[::-1])
            
            
