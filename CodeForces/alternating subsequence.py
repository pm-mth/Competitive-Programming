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

test_case = inp()
for _ in range(test_case):
    n = inp()
    nums = inlt()
    answer = []
    minm = float("-inf")
    neg, pos = minm, 0
    i = 0
    while i < n:
        while i < n and nums[i] > 0:
            pos = max(pos, nums[i])
            i += 1
        if pos:
            answer.append(pos)
        pos = 0
        while i < n and nums[i] < 0:
            neg = max(neg, nums[i])
            i += 1
        if neg != minm:
            answer.append(neg)
        neg = minm
   
    ans = sum(answer)
    print(ans)
        
