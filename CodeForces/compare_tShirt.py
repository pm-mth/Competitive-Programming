# from [smt] import [smt]
# import sys
# sys.setrecursionlimit(2000)
# from collections import Counter
 
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
        t_shirtA, t_shirtB = input().split()
        
        if t_shirtA[-1] == "L" and t_shirtB[-1] == "L":
                if len(t_shirtA) == len(t_shirtB):
                        print("=")
                elif len(t_shirtA) > len(t_shirtB):
                        print(">")
                else:
                        print("<")
        elif t_shirtA[-1] == "L":
                print(">")
        elif t_shirtB[-1] == "L":
                print("<")
        elif t_shirtA[-1] == "M" and t_shirtB[-1] == "M":
                print("=")
        elif t_shirtA[-1] == "M":
                print(">")
        elif t_shirtB[-1] == "M":
                print("<")
        else:
                if len(t_shirtA) == len(t_shirtB):
                        print("=")
                elif len(t_shirtA) > len(t_shirtB):
                        print("<")
                else:
                        print(">")
        
                
        
                
                
                        
                
