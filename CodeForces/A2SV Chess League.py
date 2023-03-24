def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
 
def insr():
    s = input()
    return(list(s[:len(s)]))
 
def invr():
    return(map(int,input().split()))
    
 
def divide(chess, k):
    if len(chess) == 1:
        return chess
    n = len(chess)
    left = divide(chess[:n//2], k)
    right = divide(chess[n//2:], k)
    
    return merge(left, right, k)
 
def merge(left, right, k):
    
    
    p1, p2 = 0, 0
    intermediate = []
 
    while  p1 < len(left) and p2 < len(right):
        if chess[left[p1]] - chess[right[p2]] > k:
            p2 += 1
        elif chess[right[p2]] - chess[left[p1]] > k:
            p1 += 1
        else:
            if chess[left[p1]] < chess[right[p2]]:
                intermediate.append(left[p1])
                p1 += 1
            else:
                intermediate.append(right[p2])
                p2 += 1
                
    intermediate.extend(left[p1:])
    intermediate.extend(right[p2:])
    
    return intermediate
            
        
n, k = invr()
chess = inlt()
n = 2**n
index = [i for i in range(n)]
 
print(*[i + 1 for i in sorted(divide(index, k))])
