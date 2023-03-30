class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        overflow = 0
        ans = []
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 and j >= 0:
            s1, s2 = int(a[i]), int(b[j])
            temp = s1 ^ s2 ^ overflow
            ans.append(str(temp))
            if s1 & s2: 
                overflow = 1
            elif s1 | s2 == 0:
                overflow = 0
            i -= 1
            j -= 1
            
        while i >= 0:
            s1 = int(a[i])
            temp = s1 ^ overflow
            if s1 & overflow:
                overflow = 1
            elif s1 | overflow:
                overflow = 0
            ans.append(str(temp))
            i -= 1
            
        while j >= 0:
            s1 = int(b[j])
            temp = s1 ^ overflow
            ans.append(str(temp))
            if s1 & overflow:
                overflow = 1
            elif s1 | overflow:
                overflow = 0
            j -= 1
        if overflow:
            ans.append(str(overflow))
        return "".join(ans[::-1])
            
            
