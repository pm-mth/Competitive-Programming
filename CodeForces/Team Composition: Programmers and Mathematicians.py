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
    
test_cases = inp()
for _ in range(test_cases):
    p, m = invr()
    min_val = min(p, m)
    left, right = -1, (p+m)//4 + 1
    while left + 1 < right:
        mid = left + (right - left)//2
        if mid <= min_val:
            left = mid
        else:
            right = mid
        
    print(left)
