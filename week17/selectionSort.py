class Solution: 
    def select(self, arr, i):
        # code here 
        cur = i
        for j in range(i, len(arr)):
            if arr[j] < arr[cur]:
                cur = j
        return cur
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            cur = self.select(arr, i)
            arr[i], arr[cur] = arr[cur], arr[i]
