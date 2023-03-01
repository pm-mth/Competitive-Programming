class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        
        for r in range(len(s)):
            if stack and stack[-1] == "(" and s[r] == ")":
                stack.pop()
                stack.append(1)
            elif stack and stack[-1] != "(" and s[r] == ")":
                add = 0
                while stack and stack[-1] != "(":
                    add += stack.pop()
                stack.pop()
                stack.append(add*2)
            else:
                stack.append(s[r])
                
        return sum(stack)
                
        
        
        