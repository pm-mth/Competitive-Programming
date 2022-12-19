n = int(input())
count = {}
for _ in range(n):
    s = input()
    if s in count.keys():
        count[s] += 1
    else:
        count[s] = 1

print(len(count))

res = ""
for val in list(count.values()):
    res += str(val) + " "
print(res)
