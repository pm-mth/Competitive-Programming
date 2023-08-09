class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = values[0]
        maxScore = -inf
        for i in range(1, len(values)):
            maxScore = max(maxScore, values[i] - i + dp)
            dp = max(values[i] + i, dp)
        
        return maxScore



        
