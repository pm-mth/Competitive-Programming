class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        score_age = [[scores[i], ages[i]] for i in range(len(ages))]
        score_age.sort(key = lambda x: (x[1], x[0]))
       

        @cache
        def dp(score, i):
            if i >= len(ages):
                return 0
            
            if score_age[i][0] < score:
                val = dp(score, i + 1)
            else:
                val = max(dp(score_age[i][0], i + 1) + score_age[i][0], dp(score, i + 1))


            return val
        
        return dp(0, 0)
        
        
        


   
        b
