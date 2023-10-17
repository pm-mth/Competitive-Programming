class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return (factorial(n + m - 2)) // (factorial(m - 1) * factorial(n -1))
        
