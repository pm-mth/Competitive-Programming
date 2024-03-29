class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        height = [0] * (n + 1)
        maxArea = 0
        
        for row in matrix:
            
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == "1" else 0
                
            stack = [-1]
            
            for i in range(n+1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    maxArea = max(maxArea, h*w)
                stack.append(i)
        return maxArea
        
