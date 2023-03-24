#import sys
#from collections import defaultdict

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))

def insr():
    s = input()
    return(list(s[:len(s)]))

def invr():
    return(map(int,input().split()))
def findBeautiArr(nums, l, r):
    if l + 1 == r:
        return [nums[l]]
    
    left = findBeautiArr(nums, l, (l + r)//2 )
    right = findBeautiArr(nums, (l +r)//2, r)
    return merge(left, right)
    
    
def merge(left, right):
    global ans
    if left[0] > right[0]:
        ans += 1
        left, right = right, left
  
    return left + right
    

test_cases = inp()
for _ in range(test_cases):
    n = inp()
    permutations = inlt()
    ans = 0
    arr = findBeautiArr(permutations, 0, n)
    if arr != sorted(permutations):
        print(-1)
    else:
        print(ans)
