class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for r in range(len(tokens)):
            if tokens[r] != "*" and tokens[r] != "+" and tokens[r] != "-" and tokens[r] != "/":
                stack.append(int(tokens[r]))
            else:
                a = stack.pop()
                b = stack.pop()
                
                if tokens[r] == "*":
                    res = a * b
                    stack.append(res)
                elif tokens[r] == "+":
                    res = a + b
                    stack.append(res)
                elif tokens[r] == "-":
                    res = b - a
                    stack.append(res)
                else:
                    res = b/a
                    if res < 0:
                        res = ceil(res)
                    else:
                        res = floor(res)
                    stack.append(res)
                    
        return stack[0]
                    
                    
        