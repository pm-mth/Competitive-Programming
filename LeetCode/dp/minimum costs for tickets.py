class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [inf for _ in range(n + 1)]
        dp[n] = 0
        for i in range(n -1, -1, -1):
            week = bisect_left(days, days[i] + 7)
            month = bisect_left(days, days[i] + 30)
            dp[i] = min( costs[1] + dp[week], costs[2] + dp[month], costs[0]+ dp[i + 1])

        return dp[0]
