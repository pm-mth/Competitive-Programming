# from [smt] import [smt]
# import sys
# sys.setrecursionlimit(2000)

# from collections import defaultdict
# from collections import deque
import heapq

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def maxRAM(ram, k):
    
    while ram:
        cur = heapq.heappop(ram)
        
        if cur[0] <= k:
            k += cur[1]
        else:
            return k
    return k

t = inp()

for _ in range(t):
    n, k = invr()
    a = inlt()
    b = inlt()
    ram = [[a[i], b[i]] for i in range(n)]
    
    heapq.heapify(ram)
    print(maxRAM(ram, k))
    
