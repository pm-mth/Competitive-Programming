class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList = path.split("/")
        stack = ["/"]
        
        for r in range(len(pathList)):
            if pathList[r] == ".." and len(stack) > 2:
                stack.pop()
                stack.pop()
            elif pathList[r] != "" and pathList[r] != "." and pathList[r] != "..":
                stack.append(pathList[r])
                stack.append("/")
                
        if stack and stack[-1] == "/" and len(stack) > 1:
            stack.pop()
        
        return "".join(stack)
        
        