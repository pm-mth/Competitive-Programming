#User function Template for python3

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
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends