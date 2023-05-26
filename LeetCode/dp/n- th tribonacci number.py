class Solution:
    def tribonacci(self, n: int) -> int:
        dp = defaultdict(int)
        def solve(n):
            if n <= 1:
                return n
            if n == 2:
                return 1
            if dp[n]:
                return dp[n]

            dp[n] = solve(n -1) + solve(n - 2) + solve(n - 3)
            return dp[n]
        return solve(n)
