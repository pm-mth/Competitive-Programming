# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int,input().split())
index = defaultdict(list)

for i in range(1, n+1):
    index[input()].append(i)

B = []
for _ in range(m):
    B.append(input())

for ch in B:
    if ch in index.keys():
        print(" ".join(map(str, index[ch])))
    else:
        print(-1)
