# from [smt] import [smt]
# import sys
# sys.setrecursionlimit(2000)
from collections import defaultdict
 
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

def check_occurance(dictionary):
        for key in dictionary.keys():
                if len(dictionary[key]) > 1:
                        return False
        return True

test_cases = inp()
for _ in range(test_cases):
        array_length = inp()
        numbers = inlt()
        letters = input()
        
        # create dictionary to store the repetation
        count = defaultdict(set)
        for i in range(array_length):
                count[numbers[i]].add(letters[i])
               
        #check the number of occurance 
        if check_occurance(count):
                print("YES")
        else:
                print("NO")
