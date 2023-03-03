class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        #count the frequency of the lexicographically smallest character in each words
        words_count = []
        for s in words:
            num = s.count(min(s))
            words_count.append(num)
        
        
        words_count.sort()
            
    
        #count the frequency of the lexicographically smallest character in each query
        
        target = []
        for s in queries:
            num = s.count(min(s))
            target.append(num)
       
        #for each query find the number of words in words 
        answer = []
        n = len(words_count)
        for num in target: 
            left, right = -1, n
            
            while right > left + 1:
                mid = left + (right - left)//2
                
                if words_count[mid] > num:
                    right = mid
                else:
                    left = mid
            answer.append(n - right)
            
        return answer
            
            
        
        
        