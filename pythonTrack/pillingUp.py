# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for _ in range(t):
    n = int(input())
    block = list(map(int, input().split()))
    
    l, r = 0, n -1
    if block[l] >= block[r]:
        prev = block[l]
        l += 1
    else:
        prev = block[r]
        r -= 1
    while l <= r:
        if block[l] >= block[r]:
            if block[l] <= prev:
                prev = block[l]
                l += 1
            else:
                break
        else:
            if block[r] <= prev:
                prev = block[r]
                r -= 1
            else:
                break
    if l > r:
        print("Yes")
    else:
        print("No")
