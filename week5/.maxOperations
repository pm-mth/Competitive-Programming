class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        
        count = defaultdict(int)
        answer = 0
        
        for num in nums:
            count[num] += 1
            
        for key in count.keys():
            comp = k - key
            if comp == key:
                answer += count[key]//2
            elif comp in count:
                answer += min(count[key], count[comp])
                count[key] = count[comp] = 0
                
            
                
            # print(count)  
            
          
        
        return answer
            
        
