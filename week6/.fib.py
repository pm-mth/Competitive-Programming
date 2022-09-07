class Solution:
    def fib(self, n: int) -> int:
        dp = defaultdict(int)
        
        def solve(n:int) -> int:
            if n <= 1:
                return n
            elif dp[n]!=0:
                return dp[n]
            else:
                dp[n] = solve(n-1) + solve(n-2)
                return dp[n]
        return solve(n)
