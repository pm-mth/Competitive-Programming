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

def isPossible(arr, n):
    if n == 1:
        return True
    for i in range(1, n):
        if arr[i] - arr[i - 1] > 1:
            return False
    return True

test_cases = inp()
for _ in range(test_cases):
    n = inp()
    arr = inlt()
    arr.sort()
    if isPossible(arr, n):
        print("YES")
    else:
        print("NO")
