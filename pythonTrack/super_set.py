# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())
flag = True
for _ in range(n):
    other_set = set(map(int, input().split()))
    flag = flag and A.issuperset(other_set)

print(flag)
        
