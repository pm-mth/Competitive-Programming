class Solution:
    def decodeString(self, s: str) -> str:
    
        def recursion(s):
            string = ""
            n = ""
            i = 0
            while i < len(s):
                if s[i] == "]":
                    return (string, i)
            
                if s[i].isnumeric():
                    n += s[i]
                if s[i] == "[":
                    inter = recursion(s[i+1:])
                    string += (int(n)*inter[0])
                    n = ""
                    i += inter[1] + 1
                if s[i].isalpha():
                    string += s[i]
                i += 1
            return (string, i)
            
        return recursion(s)[0] 
        

        
                