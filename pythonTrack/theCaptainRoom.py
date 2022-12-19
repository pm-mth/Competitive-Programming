# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
room = list(map(int, input().split()))
count = {}
for num in room:
    if num not in count.keys():
        count[num] = 1
    else:
        count[num] += 1

for key in count.keys():
    if count[key] == 1 :
        print(key)
        
