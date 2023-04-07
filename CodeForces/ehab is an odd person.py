#import sys
from collections import defaultdict
from collections import Counter
#import math

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))

def insr():
    s = input()
    return(list(s[:len(s)]))

def invr():
    return(map(int,input().split()))
def evenOrOdd(nums):
    odd, even = False, False
    for num in nums:
        odd = odd or num % 2 == 1
        even = even or num % 2 == 0
        

    return even and odd
    
n = inp()
nums = inlt()
if evenOrOdd(nums):
    print(*sorted(nums))
else:
    print(*nums)
