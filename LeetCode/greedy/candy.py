class Solution:
    def candy(self, ratings: List[int]) -> int:

        res = [1] * len(ratings)
        i = 1
        while i < len(ratings):
            intermediate_stack = []

            while i < len(ratings) and ratings[i] < ratings[i- 1]:
                intermediate_stack.append(1)
                i += 1
            
            j = i - 2
            count = 1
            while intermediate_stack:
                ans = intermediate_stack.pop() + count
                if ans > res[j]:
                    res[j] = ans
                j -= 1
                count += 1

            if i < len(ratings) and ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
            i += 1
      
        return sum(res)

            
                
