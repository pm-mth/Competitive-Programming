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
i, j = 0, 0
merge = []
while i < n and j < m:
    if nums1[i] <= nums2[j]:
        merge.append(nums1[i])
        i += 1
    else:
        merge.append(nums2[j])
        j += 1
if i >= n:
    merge.extend(nums2[j:])
else:
    merge.extend(nums1[i:])
print(*merge)
        
