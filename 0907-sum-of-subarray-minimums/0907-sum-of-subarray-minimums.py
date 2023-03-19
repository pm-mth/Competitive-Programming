class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        minSum = 0
        subarray = 0
        
        for i in range(len(arr)):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                num, acc = stack.pop()
                subarray -= num * acc
                count += acc
            
            stack.append((arr[i], count))
            subarray += arr[i] * count
            minSum += subarray
        
        return minSum % (10**9 + 7)
                
        