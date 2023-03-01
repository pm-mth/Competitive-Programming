class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for r in range(len(s)):
            if s[r] != "*":
                stack.append(s[r])
            else:
                if stack:
                    stack.pop()
        return "".join(stack)
        