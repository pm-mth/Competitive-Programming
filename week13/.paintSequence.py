# from [smt] import [smt]
# import sys
# sys.setrecursionlimit(2000)

# from collections import defaultdict
# from collections import deque

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def paintSequence(n, seq):
    
    blue = 0
    countB = 1
    sumB = seq[blue]
    red = n-1
    countR = 1
    sumR = seq[red]
    
    while blue < red:
        if countB > countR and sumR > sumB:
            return True
        if countB <= countR:
            blue += 1
            countB += 1
            sumB += seq[blue]
        if sumB >= sumR:
            red -= 1
            countR += 1
            sumR += seq[red]
    return False
    

t = inp()
for _ in range(t):
    n = inp()
    seq = inlt()
    seq.sort()
    if paintSequence(n, seq):
        print("Yes")
    else:
        print("No")


