# from [smt] import [smt]
# import sys
# sys.setrecursionlimit(2000)
# from collections import defaultdict
 
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
    
def minCost(nums,n):
        minCost = 0
        nums.sort()
        for i in range (1, n, 2):
                neg = abs(-1 - nums[i]) + abs(-1 - nums[i-1])
                pos = abs(1 - nums[i]) + abs(1 - nums[i-1])
                minCost += min(neg, pos)
        if n%2 == 0:
                return minCost
        else:
                return minCost + abs(1-nums[-1])



n = inp()
nums = inlt()
print(minCost(nums, n))
                
        
    
            
