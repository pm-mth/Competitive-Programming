class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = ["../"]
        for r in range(len(logs)):
            if logs[r] == "../" and stack[-1] != "../":
                stack.pop()
            elif logs[r] != "./":
                stack.append(logs[r])
        
        op = 0
        while stack and stack[-1] != "../":
            stack.pop()
            op += 1
        return op
                