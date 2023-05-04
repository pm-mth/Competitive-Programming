#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        large = i
        
        # code here
        left = 2 * large + 1
        right = 2 * large + 2
        
        if left < n and arr[left] > arr[large]:
            large = left
        
        if right < n and arr[right] > arr[large]:
            large = right
        
        if large != i:
            arr[large], arr[i] = arr[i], arr[large]
            self.heapify(arr, n, large)
        
        
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n//2 - 1, -1, -1):
            self.heapify(arr, n, i)
            
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr, n)
        arr[n-1], arr[0] = arr[0], arr[n - 1]
        for i in range(1, n):
            last = n - i - 1
            self.heapify(arr, n - i, 0)
            arr[last], arr[0] = arr[0], arr[last]
        
        return arr
            
        
        
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends
