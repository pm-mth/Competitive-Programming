class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = list(count.items())
        
        self.quickSort(0, len(arr) - 1, arr)
        answer = []
        for i in range(len(arr) - 1, -1,-1):
            if k <= 0:
                break
            answer.append(arr[i][0])
            k -= 1
        return answer
            
        
    def quickSort(self,l, r, arr):
        if l >= r:
            return 
        mid = l + (r - l)//2
        pivot = self.findMedian(l, r, mid, arr)
        w = l
        for r in range(l, r + 1):
            if arr[r][1] <= arr[pivot][1]:
                if r == pivot :
                    continue
                if w == pivot:
                    w += 1
                arr[w], arr[r] = arr[r], arr[w]
                w += 1
        if pivot < w:
            w -= 1
        arr[w], arr[pivot] =  arr[pivot], arr[w]
        self.quickSort(l, w - 1, arr)
        self.quickSort(w + 1, r, arr)
    def findMedian(self,a, b, c, arr):
        if arr[a][1] < arr[b][1] < arr[c][1] or arr[a][1] > arr[b][1] > arr[c][1]:
            return b
        if arr[a][1] < arr[c][1] < arr[b][1] or arr[a][1] > arr[c][1] > arr[b][1]:  
            return c
        return a
            
        
        
        
        
        