class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        smallestIndex = len(arr) - 1
        largeIndex = -1

        for i in range(len(arr) -2, -1, -1):
            if arr[i] > arr[smallestIndex]:
                largeIndex =  i
                break
            if arr[i] <= arr[smallestIndex]:
                smallestIndex = i
        
        if largeIndex == -1:
            return arr
        

        for i in range(largeIndex + 1, len(arr)):
            if arr[i] < arr[largeIndex] and arr[i] > arr[smallestIndex]:
                smallestIndex = i
        arr[largeIndex], arr[smallestIndex] = arr[smallestIndex], arr[largeIndex]

        return arr
                
            


    
