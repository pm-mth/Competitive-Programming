class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
    
       
        if len(arr) == 1:
            return False
        if arr[0] > arr[1]:
            return False
        
        i = 0
        while i <= len(arr)-1:
            while i < len(arr)-1 and  arr[i] < arr[i+1]:
                i += 1
            if i == len(arr) - 1:
                return False
            while i < len(arr)-1 and arr[i] > arr[i+1]:
                i += 1
            if i == len(arr) - 1:
                return True
            return False
            
            
            
        