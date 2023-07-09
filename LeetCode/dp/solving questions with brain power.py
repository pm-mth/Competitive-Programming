class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = defaultdict(int)
        def dfs(index):
            
            if index >= len(questions):
                return 0


            if dp[index]:
                return dp[index]
            points, brainPower = questions[index]
    
            dp[index] = max(points + dfs(index + brainPower + 1), dfs(index + 1))

            return dp[index]
        
        

        return dfs(0)
        
