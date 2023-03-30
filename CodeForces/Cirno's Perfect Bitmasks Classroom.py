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
    x = inp()
    mask = 1
    temp = x
    while mask <= x:
        if temp & mask:
            if temp ^ mask:
                ans = mask
            else:
                if mask == 1:
                    ans = mask + 2
                else:
                    ans = mask + 1
            break
        mask <<= 1
    print(ans)
            
                
        
