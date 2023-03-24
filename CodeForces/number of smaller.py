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

n, m = invr()
nums1 = inlt()
nums2 = inlt()
count = 0
i = 0
answer = []
for j in range(m):
    while i < n and nums1[i] < nums2[j]:
        i += 1
        count += 1
    if (i < n and nums1[i] >= nums2[j]) or i >= n:
        answer.append(count)
   
print(*answer)        
