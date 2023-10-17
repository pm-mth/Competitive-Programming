class Solution:
    def calculate(self, s: str) -> int:
        arr = []
        for n in s:
            if n == " ":
                continue
            arr.append(n)
        s = arr
        stack = []
        i = 0
        while i < len(s):
            
            if s[i] == '*':
                i += 1
                num = stack.pop()
                temp = ""
                while i < len(s) and s[i].isnumeric():
                    temp += s[i]
                    i += 1
                stack.append(num * int(temp))
                i -= 1
            elif s[i] == '/':
            
                i += 1
                num = stack.pop()
                temp = ""
                while i < len(s) and s[i].isnumeric():
                    temp += s[i]
                    i += 1
                i -= 1
                stack.append(num // int(temp))
            elif s[i] == '+' or s[i] == '-':
                stack.append(s[i])
            else:
                temp = ""
                while i < len(s) and s[i].isnumeric():
                    temp += s[i]
                    i += 1
                i -= 1
                stack.append(int(temp))
            i += 1
        i = 0
        res = 0
        while i < len(stack):
            if stack[i] == "+":
                i += 1
                res += stack[i]
                
            elif stack[i] == "-":
                i += 1
                res -= stack[i]
            else:
                res += stack[i]
            
            i += 1
        return res
               



        
