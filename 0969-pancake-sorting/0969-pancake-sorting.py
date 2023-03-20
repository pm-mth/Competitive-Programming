class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        index = defaultdict(int)
    
        for i in range(len(arr)):
            index[arr[i]] = i + 1
       
        answer = []
        for i in range(len(arr), 0, -1):
            idx = index[i] 
            if idx == i:
                continue
            
            
            if idx != 1:
                left, right = 0, idx - 1
                answer.append(idx)
                while left <= right:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1
            
            left, right = 0, i - 1
            answer.append(i)
            while left <= right:
                index[arr[left]] = right + 1
                index[arr[right]] = left + 1
                arr[left], arr[right] = arr[right], arr[left]
                
                left += 1
                right -= 1
        
        return answer
            
            
            
                
            
        
        
            
        
      