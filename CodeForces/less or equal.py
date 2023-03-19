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

n, k = invr()
arr = inlt()
arr.sort()


if k == 0:
    if arr[0] > 1:
        print(1)
    else:
        print(-1)
elif k == n:
    print(arr[-1])
elif k < n and arr[k - 1] != arr[k]:
    print(arr[k - 1])
else:
    print(-1)
    
    
