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
    
def solve(n, power):
    ans = []
    stren = len(power)
    for i in range(n):
        if i <= stren -1:
            ans.append(stren)
        else:
            ans.append(i+1)
    return ans
    

        

t = inp()
for _ in range(t):
    n  = inp()
    power = set(inlt())
    print(*solve(n,power))
    
            
