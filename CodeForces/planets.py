# from [smt] import [smt]
# import sys
# sys.setrecursionlimit(2000)
from collections import Counter
 
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))



test_cases = inp()
for _ in range(test_cases):
        No_planets, Second_Machine_Cost = invr()
        planet_Orbit = inlt()
        
        #The planet in each orbit is counted
        planet_count = Counter(planet_Orbit)
        
        #finding the minimum cost
        ans = 0
        for key in planet_count.keys():
                if planet_count[key] >= Second_Machine_Cost:
                        ans += Second_Machine_Cost
                else:
                        ans += planet_count[key]
        print(ans) 
        
        

        
                
        
                
                
                        
                
