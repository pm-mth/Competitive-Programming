class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        minNumber = [0] * len(rating)
        maxNumber = [0] * len(rating)
        for i in range(len(rating)):
            minNum, maxNum = 0, 0
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    maxNum += 1
                elif rating[j] < rating[i]:
                    minNum += 1
            minNumber[i] = minNum
            maxNumber[i] = maxNum
       
        res = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    res += maxNumber[j]
                else:
                    res += minNumber[j]
        
        return res



        
        
